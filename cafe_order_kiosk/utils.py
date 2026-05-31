from __future__ import annotations

from datetime import datetime, timezone


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def format_money(amount: int) -> str:
    return f"{amount:,}"
