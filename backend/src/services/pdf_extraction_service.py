import pdfplumber


class PdfExtractionService:
    def extract_text(self, file_path: str) -> str:
        parts: list[str] = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                parts.append(page.extract_text() or "")
        return "\n".join(parts).strip()
