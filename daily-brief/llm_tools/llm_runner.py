"""
تشغيل الـ LLM — نقطة اعتماد واحدة للدليل اليومي.
المشروع يعتمد أساساً على LLM؛ بدون مفتاح API لا يُنتج الدليل.
"""
import os
from typing import Optional


class LLMRunner:
    """تشغيل نموذج لغة (OpenAI) لتوليد الدليل اليومي."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-4o-mini",
    ):
        self.api_key = (api_key or os.environ.get("OPENAI_API_KEY", "")).strip()
        self.model = model
        self._client = None

    def _get_client(self):
        if self._client is not None:
            return self._client
        # الأولوية لـ env (GitHub Actions) ثم لـ self.api_key
        key = os.environ.get("OPENAI_API_KEY") or self.api_key
        key = (key or "").strip()
        if not key:
            raise RuntimeError(
                "مفتاح OpenAI مطلوب. ضع OPENAI_API_KEY في .env أو في التكوين (guide.openai_api_key)."
            )
        try:
            from openai import OpenAI
            self._client = OpenAI(api_key=key)
            return self._client
        except ImportError:
            raise RuntimeError("ثبّت openai: pip install openai")

    def complete(
        self,
        system: str,
        user: str,
        max_tokens: int = 4000,
    ) -> str:
        """يرسل system + user ويُرجع رد النموذج كنص."""
        client = self._get_client()
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            max_tokens=max_tokens,
        )
        return (response.choices[0].message.content or "").strip()

    @property
    def is_available(self) -> bool:
        return bool(os.environ.get("OPENAI_API_KEY") or self.api_key)
