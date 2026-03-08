from pathlib import Path
import zipfile


class ExportPackageService:
    def build_zip(self, output_dir: str, project_id: str, json_text: str, markdown_text: str) -> str:
        base = Path(output_dir)
        base.mkdir(parents=True, exist_ok=True)
        zip_path = base / f"{project_id}-course.zip"

        json_path = base / "course.json"
        md_path = base / "course.md"
        json_path.write_text(json_text, encoding="utf-8")
        md_path.write_text(markdown_text, encoding="utf-8")

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
            archive.write(json_path, arcname="course.json")
            archive.write(md_path, arcname="course.md")

        return str(zip_path)
