class LanguageConfirmationService:
    def requires_confirmation(self, confidence: float | None, threshold: float = 0.8) -> bool:
        if confidence is None:
            return True
        return confidence < threshold

    def detect_language(self, text: str) -> tuple[str, float]:
        lowered = text.lower()
        cyr = sum(1 for ch in lowered if "а" <= ch <= "я")
        lat = sum(1 for ch in lowered if "a" <= ch <= "z")
        if cyr == 0 and lat == 0:
            return "unknown", 0.0
        if cyr > lat:
            return "ru", min(1.0, cyr / max(1, cyr + lat) + 0.2)
        return "en", min(1.0, lat / max(1, cyr + lat) + 0.2)
