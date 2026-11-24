#!/usr/bin/env bash
set -euo pipefail

: "${STAR1AGE_API_KEY:?Set STAR1AGE_API_KEY first (https://api.star1age.cn/en/console/api-keys)}"
API_BASE="https://api.star1age.cn/v1"

# 1. List active models
curl -sS "$API_BASE/models" \
  -H "Authorization: Bearer $STAR1AGE_API_KEY" | head -c 500
echo ""

# 2. Chat completion (GPT 6.2 Sol — 80% below official list price)
curl -sS "$API_BASE/chat/completions" \
  -H "Authorization: Bearer $STAR1AGE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "star1age-gpt-6.2-sol",
    "messages": [{"role": "user", "content": "Hello from Wanyra API"}]
  }'
echo ""
