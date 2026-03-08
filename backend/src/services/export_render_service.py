import json


class ExportRenderService:
    def render_json(self, project: dict, modules: list[dict]) -> str:
        return json.dumps({"project": project, "modules": modules}, ensure_ascii=False, indent=2)

    def render_markdown(self, project: dict, modules: list[dict]) -> str:
        lines = [f"# {project['title']}", ""]
        for module in modules:
            lines.append(f"## Module {module['moduleIndex']}: {module['title']}")
            lines.append("")
            lines.append(module["summaryText"])
            lines.append("")
            lines.append("### Questions")
            for idx, q in enumerate(module.get("questions", []), start=1):
                lines.append(f"{idx}. {q['questionText']}")
            lines.append("")
        return "\n".join(lines)
