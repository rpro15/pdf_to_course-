from pathlib import Path

from ...services.pdf_extraction_service import PdfExtractionService
from .base_adapter import BaseInputAdapter


class PdfInputAdapter(BaseInputAdapter):
    def __init__(self) -> None:
        self.extractor = PdfExtractionService()

    def detect(self, source_path: str) -> bool:
        return Path(source_path).suffix.lower() == ".pdf"

    def extract_text(self, source_path: str) -> str:
        return self.extractor.extract_text(source_path)
