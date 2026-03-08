import pdfplumber


class PdfValidationService:
    def detect_source_type(self, file_path: str) -> str:
        with pdfplumber.open(file_path) as pdf:
            page_count = len(pdf.pages)
            non_empty = 0
            for page in pdf.pages:
                if (page.extract_text() or "").strip():
                    non_empty += 1
            if page_count == 0:
                return "image_pdf"
            coverage = non_empty / page_count
            return "text_pdf" if coverage >= 0.6 else "image_pdf"
