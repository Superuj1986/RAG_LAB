from pathlib import Path

from qdrant_client import QdrantClient


# Keep the local database beside the project, regardless of the working directory.
QDRANT_PATH = Path(__file__).resolve().parent / "qdrant_storage"

# Embedded/local mode: Qdrant runs inside this Python process and persists data
# in QDRANT_PATH. Do not create a second client for this path in the same process.
client = QdrantClient(path=str(QDRANT_PATH))
