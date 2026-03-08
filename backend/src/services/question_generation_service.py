from collections import Counter


class QuestionGenerationService:
    def generate(self, chapter_text: str, count: int = 8) -> list[dict[str, str]]:
        count = max(8, min(10, count))
        words = [word.lower().strip('.,:;!?()[]{}"\'') for word in chapter_text.split()]
        top_words = [w for w, _ in Counter(w for w in words if len(w) > 4).most_common(count)]
        while len(top_words) < count:
            top_words.append(f"concept-{len(top_words)+1}")

        questions: list[dict[str, str]] = []
        for i in range(count):
            q_type = ["recall", "understanding", "application"][i % 3]
            term = top_words[i]
            if q_type == "recall":
                text = f"What is the role of '{term}' in this chapter?"
            elif q_type == "understanding":
                text = f"How would you explain '{term}' using the chapter's main idea?"
            else:
                text = f"How can '{term}' be applied in a practical learning scenario?"
            questions.append({"questionText": text, "questionType": q_type})
        return questions
