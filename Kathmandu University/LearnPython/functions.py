"""Practical function examples with default arguments."""

from typing import Iterable


def greet(name: str, language: str = "en") -> str:
    greetings = {
        "en": "Hello",
        "ne": "Namaste",
        "hi": "Namaskar",
    }
    return f"{greetings.get(language, greetings['en'])}, {name}!"


def average(values: Iterable[float]) -> float:
    values = list(values)
    if not values:
        raise ValueError("average() requires at least one number")
    return sum(values) / len(values)


if __name__ == "__main__":
    print(greet("Sita"))
    print(greet("Ram", language="ne"))
    print("Average of [2, 4, 6]:", average([2, 4, 6]))
