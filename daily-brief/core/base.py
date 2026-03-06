"""
Daily Brief — Base types and abstract source.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional


@dataclass
class BriefItem:
    """عنصر واحد في الموجز."""
    kind: str  # reading | link | project | suggestion | update
    title: str
    url: str = ""
    description: str = ""
    source_name: str = ""
    metadata: dict = field(default_factory=dict)


@dataclass
class Context:
    """السياق المستخرج من New_ara."""
    phase: str = ""
    current_paper: str = ""
    current_section: str = ""
    reminders: list[str] = field(default_factory=list)
    raw: dict[str, Any] = field(default_factory=dict)


class BaseSource(ABC):
    """واجهة أساسية للمصادر. كل مصدر يُرجع قائمة BriefItem."""

    def __init__(self, source_name: str, config: dict):
        self.source_name = source_name
        self.config = config

    @abstractmethod
    def fetch(self, context: Optional[Context] = None) -> list[BriefItem]:
        """جلب العناصر. يمكن تمرير السياق من New_ara."""
        pass


class BaseContextSource(ABC):
    """مصدر يرجّع السياق فقط (مثل NewAraContextSource)."""

    def __init__(self, source_name: str, config: dict):
        self.source_name = source_name
        self.config = config

    @abstractmethod
    def get_context(self, root: Path) -> Context:
        """قراءة الملفات من root واستخراج السياق."""
        pass
