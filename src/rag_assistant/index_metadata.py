import hashlib
import json
from pathlib import Path

# This module provides functions to calculate a fingerprint of the data in the specified folder,
# save it to a metadata file, and check if the data has changed since the last fingerprint was saved. 
# This is used to determine whether the FAISS index needs to be rebuilt or can be loaded from disk. 

def calculate_file_hash(file_path: Path) -> str:
    hasher = hashlib.sha256()

    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def calculate_data_fingerprint(data_folder: str) -> dict:
    folder = Path(data_folder)
    fingerprint = {}

    for file_path in sorted(folder.iterdir()):
        if file_path.suffix.lower() in [".pdf", ".txt"]:
            fingerprint[file_path.name] = calculate_file_hash(file_path)

    return fingerprint


def load_saved_fingerprint(metadata_path: str) -> dict | None:
    path = Path(metadata_path)

    if not path.exists():
        return None

    return json.loads(path.read_text(encoding="utf-8"))


def save_fingerprint(metadata_path: str, fingerprint: dict) -> None:
    path = Path(metadata_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        json.dumps(fingerprint, indent=2),
        encoding="utf-8",
    )


def data_changed(data_folder: str, metadata_path: str) -> bool:
    current_fingerprint = calculate_data_fingerprint(data_folder)
    saved_fingerprint = load_saved_fingerprint(metadata_path)

    return current_fingerprint != saved_fingerprint