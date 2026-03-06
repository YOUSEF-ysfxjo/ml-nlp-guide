#!/usr/bin/env python3
"""
تشغيل الدليل اليومي: agents يقرؤون New_ara ويجمعون المصادر، ووكيل الدليل (LLM) يولد ملخصاً طويلاً وشاملاً. إرسال بالبريد إن وُجد تكوين.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

# تحميل المتغيرات من .env أو .env.example (بدون استبدال القيم الموجودة — مهم لـ GitHub Actions)
def _load_env():
    import os
    try:
        from dotenv import load_dotenv
        for f in (ROOT / ".env.example", ROOT / ".env"):
            if f.exists():
                load_dotenv(f, override=False)
                return
    except Exception:
        pass
    # احتياطي: قراءة يدوية — لا نستبدل متغيراً موجوداً في البيئة
    for name in (".env", ".env.example"):
        f = ROOT / name
        if f.exists():
            for line in f.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, _, v = line.partition("=")
                    key = k.strip()
                    if key not in os.environ:
                        os.environ[key] = v.strip()
            return
_load_env()

from core.orchestrator import run, load_config

CONFIG_PATH = ROOT / "config" / "sources.yaml"
CONFIG_JSON = ROOT / "config" / "sources.json"
OUTPUT_DIR = ROOT / "brief"

if __name__ == "__main__":
    path = CONFIG_JSON if CONFIG_JSON.exists() else CONFIG_PATH
    if not path.exists():
        print("لا يوجد config/sources.yaml أو config/sources.json")
        sys.exit(1)
    config = load_config(path)
    new_ara_root = ROOT / config.get("new_ara_root", "..")
    run(path, OUTPUT_DIR, new_ara_root)
