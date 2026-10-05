import json
from pathlib import Path

def save_pages_to_json(
        pages: list[dict],
        output_path: str,
) -> None:
    """
    Save extracted PDF page data to a JSON file.
    
    Args: 
        pages: List of page-level dictionaries.
        output_path: Path where the JSON file will be saved.
    """

    path = Path(output_path)

    # Create the parent directory if it doesn't exist.
    path.parent.mkdir(exist_ok=True, parents=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(
            pages,
            file,
            indent=2,
            ensure_ascii=False
        )
    print(f"Processed document saved to: {path}")