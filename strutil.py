"""Small string helpers."""

import re


def shout(text: str) -> str:
    """Return text in upper case with an exclamation mark."""
    return text.upper() + "!"


def slugify(text: str) -> str:
    """Return a URL slug for text.

    Lower-cases the text, replaces each run of characters that are not ASCII
    letters or digits with a single hyphen, and strips leading and trailing
    hyphens.
    """
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
