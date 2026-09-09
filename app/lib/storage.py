from pathlib import Path

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)


class StorageService:
    async def upload_file(self, file_path: Path, destination: str) -> str:
        logger.info("Uploading %s to %s", file_path, destination)
        if settings.STORAGE_BUCKET:
            # Integrate with S3, GCS, Azure Blob, etc.
            return f"s3://{settings.STORAGE_BUCKET}/{destination}"
        local_path = Path("app/static/uploads") / destination
        local_path.parent.mkdir(parents=True, exist_ok=True)
        local_path.write_bytes(file_path.read_bytes())
        return str(local_path)

    async def delete_file(self, path: str) -> bool:
        logger.info("Deleting file %s", path)
        return True
