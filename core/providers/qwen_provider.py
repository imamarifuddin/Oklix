"""
Qwen Provider.
"""

from dotenv import load_dotenv

import os

from openai import OpenAI

from .base_provider import BaseProvider

load_dotenv()


class QwenProvider(BaseProvider):
    """
    Alibaba DashScope Qwen Provider.
    """

    def __init__(self) -> None:

        self.api_key = os.getenv("QWEN_API_KEY")

        self.client = None

        if self.api_key:
            self.client = OpenAI(
                api_key=self.api_key,
                base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
            )

        self.default_model = "qwen-plus"

    def chat(
        self,
        prompt: str,
        system_prompt: str = "",
        model: str | None = None,
    ) -> str:

        if self.client is None:
            raise RuntimeError(
                "QWEN_API_KEY is not configured."
            )

        response = self.client.chat.completions.create(
            model=model or self.default_model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response.choices[0].message.content

    def health(self) -> bool:

        return self.client is not None

    def models(self) -> list[str]:

        return [
            "qwen-plus",
            "qwen-turbo",
            "qwen-max",
        ]