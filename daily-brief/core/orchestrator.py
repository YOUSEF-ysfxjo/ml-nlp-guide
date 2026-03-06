"""
منسّق الـ agents — يشغّل وكيل السياق، وكيل الجمع، ووكيل الدليل (LLM).
المشروع يعتمد أساساً على LLM؛ المخرجات دليل يومي واحد شامل.
"""
import os
from datetime import date
from pathlib import Path

from agents import ContextAgent, GatherAgent, GuideAgent
from core.email_sender import send_digest
from llm_tools import LLMRunner


def load_config(config_path: Path) -> dict:
    text = config_path.read_text(encoding="utf-8")
    if config_path.suffix.lower() == ".json":
        import json
        return json.loads(text)
    try:
        import yaml
        return yaml.safe_load(text) or {}
    except ModuleNotFoundError:
        import json
        alt = config_path.parent / "sources.json"
        if alt.exists():
            return json.loads(alt.read_text(encoding="utf-8"))
        raise SystemExit("ثبّت PyYAML أو استخدم config/sources.json")


def run(config_path: Path, output_dir: Path, new_ara_root: Path) -> str:
    config = load_config(config_path)
    root = new_ara_root.resolve()
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1) وكيل السياق — يقرأ New_ara
    context_files = config.get("context_files", [])
    context_agent = ContextAgent(context_files)
    context = context_agent.run(root)

    # 2) وكيل الجمع — يشغّل المصادر
    sources_config = config.get("sources", {})
    gather_agent = GatherAgent(sources_config, root)
    items_by_kind = gather_agent.run(context)

    # 3) وكيل الدليل — LLM يولد الدليل الشامل (مطلوب)
    guide_cfg = config.get("guide", {})
    api_key = guide_cfg.get("openai_api_key") or os.environ.get("OPENAI_API_KEY", "")
    model = guide_cfg.get("model", "gpt-4o-mini")
    llm = LLMRunner(api_key=api_key, model=model)
    guide_agent = GuideAgent(llm)
    guide_md = guide_agent.run(context, items_by_kind)

    # 4) حفظ الدليل
    today_str = date.today().isoformat()
    guide_file = output_dir / f"{today_str}-guide.md"
    guide_file.write_text(guide_md, encoding="utf-8")
    print("تم إنشاء الدليل:", guide_file)

    # 5) إرسال بالبريد إن وُجد تكوين
    email_cfg = config.get("email", {})
    if email_cfg.get("enabled", False) or os.environ.get("EMAIL_RECIPIENT"):
        subject = f"دليلك اليوم — {today_str}"
        if send_digest(subject, guide_md):
            print("تم إرسال الدليل بالبريد.")

    return str(guide_file)
