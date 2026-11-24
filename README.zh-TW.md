# Davro 與萬鑰（Wanyra）API 開發者範例與即時費率工具

[English](./README.md) | **繁體中文**

本倉庫提供零依賴的即時模型費率計算 CLI 與 OpenAI 相容 SDK 實戰範例，協助開發者透過同一份不訂閱、永不過期的點數餘額（人民幣 `1 元 = 1,000 點`），呼叫 **81+ 主流多模態 AI 模型**（Claude、GPT-6、Gemini 4、DeepSeek、通義千問、Grok，以及 Kling、Vidu、Seedance、Wan、MiniMax H3 影片／生圖／語音模型）。

## 三站產品矩陣（共用單一 Star1Age 帳號與餘額）

| 產品 | 網址 | 形態 | 最適合的場景 |
| --- | --- | --- | --- |
| **Davro Desktop** | [davro.app](https://davro.app/zh-TW/agent) | Windows 10/11 x64 桌面 AI 智能體 | 本機 Excel／PDF／簡報／程式碼自動化、AI 漫畫與短劇工作流、授權資安測試模式 |
| **Davro Cloud** | [cloud.star1age.cn](https://cloud.star1age.cn/zh-TW) | Web／Android 雲端聊天與非同步工作空間 | 隨時多模型對話、背景長任務、AI 數位員工、排程記憶、Vault 密鑰保護、橋接桌面 |
| **萬鑰 API（Wanyra）** | [api.star1age.cn](https://api.star1age.cn/zh-TW) | OpenAI 相容多模態開放 API（`https://api.star1age.cn/v1`） | 將 81+ 文字、生圖、影片、語音、向量與聯網搜尋模型整合進自有系統 |

## 快速使用即時模型費率與訂閱對比 CLI（免 API Key、零依賴）

```bash
# 即時查詢所有公開文字模型的精確點數、人民幣單價與官方折數
python tools/model_price_calc.py

# 試算每月 Token 用量與 $60/月多重訂閱（ChatGPT + Claude + Gemini）的實際價差
python tools/model_price_calc.py --estimate --model star1age-gpt-6.2-sol --input-m 2.0 --output-m 0.5
```

## SDK 範例索引

- Python 多模型切換與串流用量：[`examples/python/chat_multi_model.py`](./examples/python/chat_multi_model.py)
- Python 多模態非同步（`Idempotency-Key` + HTTP 202 輪詢生圖、影片 `multipart/form-data`、聯網搜尋）：[`examples/python/multimodal_async.py`](./examples/python/multimodal_async.py)
- Node.js OpenAI SDK：[`examples/node/quickstart.mjs`](./examples/node/quickstart.mjs)
- cURL 快速呼叫：[`examples/curl/quickstart.sh`](./examples/curl/quickstart.sh)
- 桌面版 vs 雲端版對照：[`docs/desktop-vs-cloud.md`](./docs/desktop-vs-cloud.md)

更多完整指南請見：[davro.app/zh-TW/guides](https://davro.app/zh-TW/guides) 與 [davro.app/zh-TW/models](https://davro.app/zh-TW/models)。
