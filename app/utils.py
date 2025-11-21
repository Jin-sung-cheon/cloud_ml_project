def optimize_tokens(text: str):
    cleaned = ''.join(c.lower() for c in text if c.isalnum() or c == " ")
    cleaned = " ".join(cleaned.split())
    return cleaned
