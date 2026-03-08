class QualityScoreService:
    def score(self, summary_text: str, chapter_text: str) -> int:
        if not summary_text.strip():
            return 0
        chapter_words = max(1, len(chapter_text.split()))
        summary_words = len(summary_text.split())
        compression_ratio = summary_words / chapter_words

        if compression_ratio <= 0.05:
            ratio_score = 55
        elif compression_ratio <= 0.2:
            ratio_score = 75
        elif compression_ratio <= 0.4:
            ratio_score = 85
        else:
            ratio_score = 65

        keyword_overlap = len(set(summary_text.lower().split()) & set(chapter_text.lower().split()))
        overlap_score = min(100, keyword_overlap)
        return int((ratio_score * 0.6) + (overlap_score * 0.4))

    def requires_review(self, score: int) -> bool:
        return score < 70
