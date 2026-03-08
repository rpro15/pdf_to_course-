import re


class ChapterSegmentationService:
    pattern = re.compile(r"(?im)^\s*(chapter|глава)\s+\d+.*$")

    def segment(self, text: str) -> list[tuple[str, str]]:
        lines = text.splitlines()
        boundaries: list[int] = [i for i, line in enumerate(lines) if self.pattern.match(line)]
        if not boundaries:
            return [("Chapter 1", text)]

        boundaries.append(len(lines))
        result: list[tuple[str, str]] = []
        for idx in range(len(boundaries) - 1):
            start = boundaries[idx]
            end = boundaries[idx + 1]
            title = lines[start].strip() or f"Chapter {idx + 1}"
            body = "\n".join(lines[start:end]).strip()
            result.append((title, body))
        return result
