"""Basic text file read/write patterns using context managers."""

from pathlib import Path

TEMP_FILE = Path("sample_notes.txt")


def write_sample(text: str) -> None:
    with TEMP_FILE.open("w", encoding="utf-8") as handle:
        handle.write(text)


def read_sample() -> str:
    if not TEMP_FILE.exists():
        return "No file created yet."
    with TEMP_FILE.open("r", encoding="utf-8") as handle:
        return handle.read()


if __name__ == "__main__":
    write_sample("Hamro University welcomes you to Python basics.\n")
    print("File contents:")
    print(read_sample())
