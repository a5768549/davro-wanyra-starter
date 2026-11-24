#!/usr/bin/env python3
"""
Zero-dependency CLI to inspect live Wanyra / Davro model pricing (CNY 1 = 1,000 points)
and compare pay-as-you-go token spend against stacked $20/month AI subscriptions.

Catalog source: https://api.star1age.cn/api/portal/public-api/catalog
Related sites:
  - Davro Desktop: https://davro.app
  - Davro Cloud:   https://cloud.star1age.cn
  - Wanyra API:    https://api.star1age.cn
"""

import argparse
import json
import sys
import urllib.request

CATALOG_URL = "https://api.star1age.cn/api/portal/public-api/catalog"
POINTS_PER_CNY = 1000.0
DEFAULT_USD_TO_CNY = 7.2


def fetch_catalog() -> list[dict]:
    req = urllib.request.Request(
        CATALOG_URL,
        headers={"User-Agent": "davro-wanyra-price-calc/1.0"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    return [
        m
        for m in payload.get("models", [])
        if m.get("status") == "ga" and "internal" not in (m.get("displayName") or "").lower()
    ]


def extract_text_rate(model: dict) -> dict | None:
    if model.get("endpoint") != "text":
        return None
    pricing = model.get("pricing") or []
    billing = (pricing[0].get("dimensions") or {}).get("billing") if pricing else None
    if not billing:
        return None
    comps = billing.get("components") or []

    def per_million(meter: str) -> float | None:
        for c in comps:
            if c.get("meter") == meter:
                pts = float(c.get("points", 0))
                basis = float(c.get("basis", 0))
                if basis > 0:
                    return pts * 1_000_000.0 / basis
        return None

    mult = billing.get("priceMultiplier")
    disc = billing.get("discountRate")
    if mult and float(mult) > 0:
        ratio = float(mult)
    elif disc and float(disc) > 0:
        r = float(disc)
        ratio = r / 10.0 if r > 1.0 else r
    else:
        ratio = 1.0

    in_pts = per_million("input_tokens")
    out_pts = per_million("output_tokens")
    if in_pts is None or out_pts is None:
        return None
    name = (model.get("displayName") or model["id"]).split(" (", 1)[0].strip()
    return {
        "id": model["id"],
        "name": name,
        "ratio": ratio,
        "input_pts": in_pts,
        "output_pts": out_pts,
        "input_cny": in_pts / POINTS_PER_CNY,
        "output_cny": out_pts / POINTS_PER_CNY,
    }


def fmt_cny(val: float) -> str:
    return f"CNY {val:.6f}".rstrip("0").rstrip(".")


def cmd_list(models: list[dict], keyword: str | None) -> None:
    rows = [r for m in models if (r := extract_text_rate(m))]
    if keyword:
        kw = keyword.lower()
        rows = [r for r in rows if kw in r["id"].lower() or kw in r["name"].lower()]
    if not rows:
        print("No matching GA text models found.", file=sys.stderr)
        sys.exit(1)

    print(f"{'Model':<28} {'Model ID':<34} {'Input /1M':<14} {'Output /1M':<14} {'Vs Official'}")
    print("-" * 106)
    for r in rows:
        vs = f"{round((1 - r['ratio']) * 100)}% off" if r["ratio"] < 1 else "List price"
        print(
            f"{r['name']:<28} {r['id']:<34} "
            f"{fmt_cny(r['input_cny']):<14} {fmt_cny(r['output_cny']):<14} {vs}"
        )


def cmd_estimate(models: list[dict], model_id: str, input_m: float, output_m: float, sub_usd: float) -> None:
    rows = {r["id"]: r for m in models if (r := extract_text_rate(m))}
    target = rows.get(model_id)
    if not target:
        matches = [r for k, r in rows.items() if model_id.lower() in k.lower() or model_id.lower() in r["name"].lower()]
        if len(matches) == 1:
            target = matches[0]
        else:
            print(f"Model '{model_id}' not found. Run without --estimate to list valid IDs.", file=sys.stderr)
            sys.exit(1)

    payg_pts = input_m * target["input_pts"] + output_m * target["output_pts"]
    payg_cny = payg_pts / POINTS_PER_CNY
    sub_cny = sub_usd * DEFAULT_USD_TO_CNY
    savings = sub_cny - payg_cny

    print(f"Model:          {target['name']} ({target['id']})")
    print(f"Workload:       {input_m:g}M input tokens + {output_m:g}M output tokens")
    print(f"Pay-as-you-go:  {payg_pts:,.0f} points = {fmt_cny(payg_cny)} (non-expiring)")
    print(f"Subscriptions:  ${sub_usd:g}/mo (~CNY {sub_cny:.2f}/mo, resets monthly)")
    if savings >= 0:
        print(f"Estimated save: CNY {savings:.2f}/mo ({(savings / sub_cny) * 100:.1f}% lower)")
    else:
        print(f"Difference:     CNY {-savings:.2f}/mo above ${sub_usd:g} fixed budget")


def main() -> None:
    parser = argparse.ArgumentParser(description="Live Davro / Wanyra model price lookup and cost estimator")
    parser.add_argument("--filter", help="Filter models by keyword (e.g. claude, gpt, gemini, deepseek)")
    parser.add_argument("--estimate", action="store_true", help="Estimate workload cost vs. monthly subscriptions")
    parser.add_argument("--model", default="star1age-gpt-6.2-sol", help="Model ID for --estimate")
    parser.add_argument("--input-m", type=float, default=2.0, help="Monthly input volume in millions of tokens")
    parser.add_argument("--output-m", type=float, default=0.5, help="Monthly output volume in millions of tokens")
    parser.add_argument("--sub-usd", type=float, default=60.0, help="Comparison monthly subscription spend in USD (default: $60 for 3x $20 plans)")
    args = parser.parse_args()

    models = fetch_catalog()
    if args.estimate:
        cmd_estimate(models, args.model, args.input_m, args.output_m, args.sub_usd)
    else:
        cmd_list(models, args.filter)


if __name__ == "__main__":
    main()
