#!/usr/bin/env python3
"""
تشغيل الدليل اليومي يومياً الساعة 8 صباحاً بتوقيت السعودية (UTC+3)، ثم إرسال الإيميل.
شغّل هذا السكربت واتركه يعمل، أو استخدم Task Scheduler لتشغيل run_brief.py يومياً الساعة 8 ص.
"""
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

def _load_env():
    try:
        from dotenv import load_dotenv
        for f in (ROOT / ".env.example", ROOT / ".env"):
            if f.exists():
                load_dotenv(f, override=True)
                return
    except Exception:
        pass
    for name in (".env", ".env.example"):
        f = ROOT / name
        if f.exists():
            import os
            for line in f.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, _, v = line.partition("=")
                    os.environ[k.strip()] = v.strip()
            return
_load_env()

from core.orchestrator import run, load_config

CONFIG_JSON = ROOT / "config" / "sources.json"
CONFIG_PATH = ROOT / "config" / "sources.yaml"
OUTPUT_DIR = ROOT / "brief"


def now_saudi():
    """الوقت الحالي بتوقيت السعودية."""
    try:
        from zoneinfo import ZoneInfo
        from datetime import datetime
        return datetime.now(ZoneInfo("Asia/Riyadh"))
    except ImportError:
        from datetime import datetime, timezone, timedelta
        return datetime.now(timezone.utc) + timedelta(hours=3)


def main():
    config_path = CONFIG_JSON if CONFIG_JSON.exists() else CONFIG_PATH
    if not config_path.exists():
        print("لا يوجد ملف تكوين.")
        sys.exit(1)
    config = load_config(config_path)
    new_ara_root = ROOT / config.get("new_ara_root", "..")
    last_run_date = None

    print("الجدولة مفعّلة: تشغيل الدليل كل يوم الساعة 8:00 صباحاً (توقيت السعودية).")
    print("لإيقاف: Ctrl+C\n")

    while True:
        n = now_saudi()
        # تشغيل بين 8:00 و 8:14 مرة واحدة فقط في اليوم
        if n.hour == 8 and n.minute < 15:
            today = n.date().isoformat()
            if last_run_date != today:
                try:
                    print(f"[{n.strftime('%Y-%m-%d %H:%M')}] تشغيل الدليل وإرسال الإيميل...")
                    run(config_path, OUTPUT_DIR, new_ara_root)
                    last_run_date = today
                except Exception as e:
                    print("خطأ:", e)
        time.sleep(600)  # فحص كل 10 دقائق


if __name__ == "__main__":
    main()
