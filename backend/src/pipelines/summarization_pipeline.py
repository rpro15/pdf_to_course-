class SummarizationPipeline:
    def summarize(self, chapter_text: str, target_words_min: int = 350, target_words_max: int = 700) -> str:
        words = chapter_text.split()
        if len(words) <= target_words_max:
            return chapter_text
        target_len = max(target_words_min, min(target_words_max, len(words) // 3))
        return " ".join(words[:target_len]).strip()
