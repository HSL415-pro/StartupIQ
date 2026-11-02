"""
StartupIQ Text Preprocessing Utilities
"""
import re
import string

def clean_text(text: str) -> str:
    """Cleans and standardizes raw user text."""
    if not text:
        return ""
    # Convert to lowercase
    text = text.lower()
    # Replace URLs
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    # Remove HTML tags if any
    text = re.sub(r"<.*?>", " ", text)
    # Replace punctuation with spaces
    text = text.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
    # Collapse multiple whitespaces
    text = re.sub(r"\s+", " ", text).strip()
    return text

def build_composite_text(name: str, desc: str, problem: str, audience: str = "", stack: str = "") -> str:
    """Constructs enriched representation for NLP vectorizers."""
    parts = [
        f"Startup: {name}",
        f"Description: {desc}",
        f"Problem: {problem}",
    ]
    if audience:
        parts.append(f"Target Audience: {audience}")
    if stack:
        parts.append(f"Tech Stack: {stack}")
    return " | ".join(parts)
