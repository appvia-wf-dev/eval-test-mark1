"""Small string helpers."""


def shout(text: str) -> str:
    """Return text in upper case with an exclamation mark."""
    return text.upper() + "!"


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    return len(text.split())
