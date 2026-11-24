from pathlib import Path

PICK = b"A"

Path("/output/entry.txt").write_bytes(PICK)
