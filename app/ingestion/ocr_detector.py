
def needs_ocr(text: str, min_text_chars: int  = 50) -> bool:
    """
    Determine if OCR is needed based on the extracted text.

    Args:
        text: The extracted text from a PDF page.
        min_text_chars: Minimum number of characters to consider the text valid.

    Returns: True if the page likely requires OCR, False otherwise.
    """

    meaningful_text = "".join(text.split())

    return len(meaningful_text) < min_text_chars