# Davro & Wanyra API Starter Kit

[![Davro Desktop](https://img.shields.io/badge/Davro_Desktop-davro.app-ff7a3d)](https://davro.app/en/agent)
[![Davro Cloud](https://img.shields.io/badge/Davro_Cloud-cloud.star1age.cn-1c1c1c)](https://cloud.star1age.cn/en)
[![Wanyra API](https://img.shields.io/badge/Wanyra_API-api.star1age.cn-2563eb)](https://api.star1age.cn/en)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **English** | [繁體中文](./README.zh-TW.md)

Open-source CLI tools and OpenAI-compatible SDK examples for using **81+ multimodal AI models** (Anthropic Claude, OpenAI GPT-6, Google Gemini 4, DeepSeek, Alibaba Qwen, xAI Grok, plus Kling, Vidu, Seedance, Wan, and MiniMax H3 video/image/audio models) under **one non-expiring pay-as-you-go balance** (`CNY 1 = 1,000 points`, no monthly subscription).

## Ecosystem Overview

| Product | URL | Purpose | Best For |
| --- | --- | --- | --- |
| **Davro Desktop** | [davro.app](https://davro.app/en/agent) | Windows 10/11 x64 multi-model AI agent | Local Excel/PDF/PPT/code automation, AI comics & short dramas (`make_comic` / `make_drama`), authorized security testing (`scope_check`) |
| **Davro Cloud** | [cloud.star1age.cn](https://cloud.star1age.cn/en) | Web & Android multi-model chat + async workspace | Anytime chat, background cloud tasks, AI digital employees, scheduled memory, Vault secret isolation, paired desktop bridge |
| **Wanyra API** | [api.star1age.cn](https://api.star1age.cn/en) | OpenAI-compatible unified API gateway (`https://api.star1age.cn/v1`) | Integrating 81+ text, image, video, audio, embedding, vision, and web-search models into production apps |

All three share **one Star1Age account and one credit wallet** (Alipay, WeChat Pay, and USDT TRC20 supported starting at CNY 10; points never expire).

---

## Live Pay-As-You-Go Sample Rates (Per 1M Tokens)

Run `python tools/model_price_calc.py` at any time to query the live catalog (`https://api.star1age.cn/api/portal/public-api/catalog`). Snapshot highlights (`CNY 1 = 1,000 points`, exact integer points):

| Model | API Model ID | Input (pts / CNY) | Output (pts / CNY) | Vs. Official List | Detail Page |
| --- | --- | ---: | ---: | --- | --- |
| Claude Opus 5.5 | `star1age-claude-opus-5.5` | 14,400 (CN¥14.4) | 72,000 (CN¥72) | **50% off** | [Spec & Guide](https://davro.app/en/models/claude-opus-5.5) |
| Claude Sonnet 5.5 | `star1age-claude-sonnet-5.5` | 7,200 (CN¥7.2) | 36,000 (CN¥36) | **50% off** | [Spec & Guide](https://davro.app/en/models/claude-sonnet-5.5) |
| GPT 6.2 Sol | `star1age-gpt-6.2-sol` | 2,880 (CN¥2.88) | 14,400 (CN¥14.4) | **80% off** | [Spec & Guide](https://davro.app/en/models/gpt-6.2-sol) |
| GPT 6.2 Astra | `star1age-gpt-6.2-astra` | 11,520 (CN¥11.52) | 57,600 (CN¥57.6) | **80% off** | [Spec & Guide](https://davro.app/en/models/gpt-6.2-astra) |
| Gemini 4 Neon | `star1age-gemini-4-neon` | 8,100 (CN¥8.1) | 40,500 (CN¥40.5) | **62.5% off** | [Spec & Guide](https://davro.app/en/models/gemini-4-neon) |
| Gemini 4 Carbon | `star1age-gemini-4-carbon` | 5,400 (CN¥5.4) | 27,000 (CN¥27) | **62.5% off** | [Spec & Guide](https://davro.app/en/models/gemini-4-carbon) |
| DeepSeek V4.1 Flash | `star1age-deepseek-v4.1-flash` | 800 (CN¥0.8) | 3,200 (CN¥3.2) | **20% off** | [Spec & Guide](https://davro.app/en/models/deepseek-v4.1-flash) |
| Qwen3.8 Max | `star1age-qwen3.8-max` | 12,000 (CN¥12) | 36,000 (CN¥36) | List price | [Spec & Guide](https://davro.app/en/models/qwen3.8-max) |

> Full real-time table: [davro.app/en/pricing](https://davro.app/en/pricing) · [api.star1age.cn/en](https://api.star1age.cn/en)

---

## 1. Zero-Dependency Live Price & Subscription Calculator CLI

No API key or third-party packages required — uses only Python's standard library:

```bash
# List every live GA text model with exact CNY prices and discounts
python tools/model_price_calc.py

# Estimate a custom monthly token workload and compare vs. $60/mo stacked subscriptions
python tools/model_price_calc.py --estimate --model star1age-gpt-6.2-sol --input-m 2.0 --output-m 0.5

# Filter by provider family (claude, gpt, gemini, deepseek, qwen, grok)
python tools/model_price_calc.py --filter claude
```

## 2. Quickstart SDK Examples

Set your API key from the [Wanyra API Console](https://api.star1age.cn/en/console/api-keys):

```bash
export STAR1AGE_API_KEY="sk-..."
```

- **Python multi-model chat & streaming usage**: [`examples/python/chat_multi_model.py`](./examples/python/chat_multi_model.py)
- **Python multimodal async (Images with `Idempotency-Key` + HTTP 202 polling, Video `multipart/form-data`, Web Search)**: [`examples/python/multimodal_async.py`](./examples/python/multimodal_async.py)
- **Node.js OpenAI SDK quickstart**: [`examples/node/quickstart.mjs`](./examples/node/quickstart.mjs)
- **cURL cheat sheet**: [`examples/curl/quickstart.sh`](./examples/curl/quickstart.sh)

## 3. Architecture & Comparison Notes

- [Davro Desktop vs. Davro Cloud](./docs/desktop-vs-cloud.md) — When to run tasks locally on Windows vs. asynchronously in the cloud
- [Live Product Guides on davro.app](https://davro.app/en/guides) — Multi-model selection, Poe/Cherry Studio comparison, AI comic & short drama workflows
- Machine-readable `llms.txt` endpoints:
  - [`https://davro.app/llms.txt`](https://davro.app/llms.txt)
  - [`https://cloud.star1age.cn/llms.txt`](https://cloud.star1age.cn/llms.txt)
  - [`https://api.star1age.cn/llms.txt`](https://api.star1age.cn/llms.txt)

## License

MIT — see [LICENSE](./LICENSE).

## Live Model Health & Guides

- **Wanyra Live Model Availability & Verification**: [https://api.star1age.cn/status](https://api.star1age.cn/status) (`https://api.star1age.cn/api/portal/public-api/model-health`)
- **Integration Guides (Cherry Studio / Cursor / Cline)**: [https://api.star1age.cn/guides](https://api.star1age.cn/guides)
