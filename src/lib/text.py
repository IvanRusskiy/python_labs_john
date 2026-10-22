"""Модуль текстовой обработки (ЛР3)."""

from __future__ import annotations

import re
from collections import Counter


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализует текст: casefold, ё→е, схлопывание пробелов."""
    if not isinstance(text, str):
        raise TypeError("normalize: ожидается str")

    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    text = re.sub(r" +", " ", text).strip()
    return text


def tokenize(text: str) -> list[str]:
    """Разбивает текст на слова по шаблону \\w+(?:-\\w+)*."""
    if not isinstance(text, str):
        raise TypeError("tokenize: ожидается str")
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Считает частоты слов."""
    if not isinstance(tokens, (list, tuple)):
        raise TypeError("count_freq: ожидается list[str]")
    return dict(Counter(tokens))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Топ-N: по убыванию частоты, при равенстве — по алфавиту."""
    if not isinstance(freq, dict):
        raise TypeError("top_n: ожидается dict[str, int]")
    if not isinstance(n, int) or n < 0:
        raise TypeError("top_n: n должен быть неотрицательным int")
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]