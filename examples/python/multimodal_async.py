"""
Durable multimodal examples for Wanyra API (https://api.star1age.cn/v1):
  1. Image generation with Idempotency-Key + HTTP 202 async polling
  2. Video generation with multipart/form-data
  3. Live web search endpoint

Docs: https://davro.app/en/developers | https://api.star1age.cn/en/docs
"""

import os
import time
import uuid
import requests

API_BASE = "https://api.star1age.cn/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['STAR1AGE_API_KEY']}"}


def poll_request(request_id: str, timeout_s: int = 300) -> dict:
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        resp = requests.get(f"{API_BASE}/requests/{request_id}", headers=HEADERS, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        status = data.get("status")
        if status in ("succeeded", "failed", "cancelled"):
            return data
        time.sleep(3)
    raise TimeoutError(f"Request {request_id} did not finish within {timeout_s}s")


def generate_image(prompt: str) -> dict:
    resp = requests.post(
        f"{API_BASE}/images/generations",
        headers={**HEADERS, "Idempotency-Key": f"img-{uuid.uuid4().hex}"},
        json={"model": "star1age-gpt-image-2", "prompt": prompt},
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()
    if resp.status_code == 202 and data.get("request_id"):
        return poll_request(data["request_id"])
    return data


def generate_video(prompt: str, model: str = "star1age-kling-3.0-omni") -> dict:
    resp = requests.post(
        f"{API_BASE}/videos",
        headers={**HEADERS, "Idempotency-Key": f"vid-{uuid.uuid4().hex}"},
        files={
            "model": (None, model),
            "prompt": (None, prompt),
        },
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()
    if resp.status_code == 202 and data.get("request_id"):
        return poll_request(data["request_id"], timeout_s=600)
    return data


def web_search(query: str) -> dict:
    resp = requests.post(
        f"{API_BASE}/web-search",
        headers={**HEADERS, "Idempotency-Key": f"web-{uuid.uuid4().hex}"},
        json={"model": "star1age-web-search", "query": query},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    print(web_search("Davro AI desktop agent"))
