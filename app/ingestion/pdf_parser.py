from pathlib import Path
from app.ingestion.json_writer import save_pages_to_json

import pymupdf


def extract_pdf_pages(pdf_path: str) -> list[dict]:
    """
    Extract text and metadata from a digital PDF page by page.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        A list of dictionaries containing page-level text and metadata.
    """

    path = Path(pdf_path)

    # Validate that the file exists.
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    # Validate that the file is a PDF.
    if path.suffix.lower() != ".pdf":
        raise ValueError("The provided file must be a PDF.")

    pages = []

    with pymupdf.open(path) as document:
        total_pages = len(document)

        for page_number, page in enumerate(document, start=1):
            text = page.get_text()

            page_data = {
                "file_name": path.name,
                "page_number": page_number,
                "total_pages": total_pages,
                "character_count": len(text),
                "extraction_method": "native",
                "text": text,
            }

            pages.append(page_data)

    return pages


if __name__ == "__main__":
    pdf_path = "data/sample/sample_manual.pdf"

    extracted_pages = extract_pdf_pages(pdf_path)

    print(f"File: {extracted_pages[0]['file_name']}")
    print(f"Total Pages: {extracted_pages[0]['total_pages']}")
    print("=" * 60)

    for page in extracted_pages:
        print(f"\nPage: {page['page_number']}")
        print(f"Extraction method: {page['extraction_method']}")
        print(f"Characters extracted: {page['character_count']}")
        print("-" * 60)

        print("Preview of extracted text:")
        print(page["text"][:500])

    # Save the extracted pages to a JSON file.
    save_pages_to_json(
        extracted_pages,
        "data/processed/sample_manual.json",
    )