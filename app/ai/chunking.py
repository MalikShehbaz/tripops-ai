


def chunk_text(
        text: str,
        chunk_size = 1000,
        overlap = 150
)->list[str]:


    if chunk_size <= 0:
        raise ValueError(
            "chunk size must be positive."
        )

    if overlap >= chunk_size or overlap == 0:
        raise ValueError(
            "overlap must be non zero and smaller than chunk size"
        )


    words = text.strip()
    if not words:
        raise ValueError(
            "text is require for generating chunks"
        )


    start = 0
    step = chunk_size - overlap
    chunks = []

    while start != len(words):
        chunk = " ".join(words[start:start + chunk_size])

        if chunk:
            chunks.append(chunk)

        start += step


    return chunks