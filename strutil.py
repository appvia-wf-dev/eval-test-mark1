"""Small string helpers."""


def shout(text: str) -> str:
    """Return text in upper case with an exclamation mark."""
    return text.upper() + "!"


def truncate(text: str, width: int) -> str:
    """Return text cut to at most width characters, ending in "..." when it is cut."""
    if len(text) <= width:
        return text
    return text[: width - 2] + "..."
