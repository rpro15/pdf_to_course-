from dataclasses import dataclass
from uuid import UUID

from ..pipelines.summarization_pipeline import SummarizationPipeline
from ..services.chapter_segmentation_service import ChapterSegmentationService
from ..services.quality_score_service import QualityScoreService
from ..services.question_generation_service import QuestionGenerationService


@dataclass
class GeneratedModule:
    project_id: UUID
    module_index: int
    title: str
    summary_text: str
    quality_score: int
    review_required: bool
    questions: list[dict[str, str]]


class ProcessProjectWorker:
    def __init__(self) -> None:
        self.segmenter = ChapterSegmentationService()
        self.summarizer = SummarizationPipeline()
        self.quality = QualityScoreService()
        self.question_generator = QuestionGenerationService()

    def process_text(self, project_id: UUID, text: str) -> list[GeneratedModule]:
        modules: list[GeneratedModule] = []
        for index, (title, chapter_body) in enumerate(self.segmenter.segment(text), start=1):
            summary = self.summarizer.summarize(chapter_body)
            score = self.quality.score(summary, chapter_body)
            questions = self.question_generator.generate(chapter_body)
            modules.append(
                GeneratedModule(
                    project_id=project_id,
                    module_index=index,
                    title=title,
                    summary_text=summary,
                    quality_score=score,
                    review_required=self.quality.requires_review(score),
                    questions=questions,
                )
            )
        return modules
