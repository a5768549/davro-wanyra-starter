"""
Multi-model chat and streaming usage example via the OpenAI-compatible Wanyra API.
Get an API key at https://api.star1age.cn/en/console/api-keys
"""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["STAR1AGE_API_KEY"],
    base_url="https://api.star1age.cn/v1",
)

MODELS = [
    "star1age-gpt-6.2-sol",
    "star1age-claude-sonnet-5.5",
    "star1age-gemini-4-carbon",
    "star1age-deepseek-v4.1-flash",
]


def compare_models(prompt: str) -> None:
    for model_id in MODELS:
        print(f"\n=== {model_id} ===")
        stream = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
            stream_options={"include_usage": True},
        )
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
            if chunk.usage:
                print(
                    f"\n[usage] prompt={chunk.usage.prompt_tokens}, "
                    f"completion={chunk.usage.completion_tokens}"
                )


if __name__ == "__main__":
    compare_models("Summarize the trade-offs of pay-as-you-go vs. monthly AI subscriptions in 3 bullet points.")
