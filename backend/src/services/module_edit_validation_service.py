class ModuleEditValidationService:
    def validate_summary(self, summary_text: str) -> None:
        if not summary_text.strip():
            raise ValueError("Summary text cannot be empty")

    def validate_questions(self, questions: list[dict]) -> None:
        if not questions:
            raise ValueError("At least one question is required")
        for question in questions:
            if not question.get("questionText", "").strip():
                raise ValueError("Question text cannot be empty")
