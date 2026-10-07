import os

import pymupdf


def extract_text_with_ocr(
    page: pymupdf.Page,
    language: str = "eng",
    dpi: int = 300,
) -> str:
    """
    Extract text from an image-based PDF page using OCR.

    Args:
        page: PyMuPDF page object.
        language: Tesseract OCR language.
        dpi: Resolution used during OCR.

    Returns:
        OCR-extracted text.
    """

    tessdata_path = os.getenv("TESSDATA_PREFIX")

    text_page = page.get_textpage_ocr(
        language=language,
        dpi=dpi,
        full=True,
        tessdata=tessdata_path,
    )

    text = page.get_text(textpage=text_page)

    return text