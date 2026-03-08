import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";

import { LanguageConfirmationDialog } from "../components/LanguageConfirmationDialog";
import { ModelProfileSelector } from "../components/ModelProfileSelector";
import { API_BASE_URL, apiRequest } from "../services/apiClient";

type ProjectPayload = {
  id: string;
  status: string;
  detectedLanguage?: string;
  languageConfirmationRequired?: boolean;
};

export function UploadProcessPage() {
  const navigate = useNavigate();

  const [title, setTitle] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [modelProfileId, setModelProfileId] = useState("00000000-0000-0000-0000-000000000001");

  const [project, setProject] = useState<ProjectPayload | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState("");

  const processProject = async (projectId: string) => {
    await apiRequest(`/projects/${projectId}/process`, {
      method: "POST",
      body: JSON.stringify({ modelProfileId }),
    });
    navigate(`/projects/${projectId}/modules`);
  };

  const uploadProject = async (): Promise<ProjectPayload> => {
    if (!file) {
      throw new Error("Please choose a PDF file");
    }

    const formData = new FormData();
    formData.append("title", title || file.name.replace(".pdf", ""));
    formData.append("file", file);

    const response = await fetch(`${API_BASE_URL}/projects`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(await response.text());
    }

    return (await response.json()) as ProjectPayload;
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setError("");
    setIsSubmitting(true);
    try {
      const created = await uploadProject();
      setProject(created);
      if (!created.languageConfirmationRequired) {
        await processProject(created.id);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Upload failed");
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleLanguageConfirm = async (language: string) => {
    if (!project) {
      return;
    }
    await apiRequest(`/projects/${project.id}/language-confirmation`, {
      method: "PATCH",
      body: JSON.stringify({ confirmedLanguage: language }),
    });
    await processProject(project.id);
  };

  return (
    <main style={{ maxWidth: 760, margin: "0 auto", padding: 20 }}>
      <h1>PDF to Course MVP</h1>
      <form onSubmit={handleSubmit}>
        <label style={{ display: "block", marginBottom: 12 }}>
          <div>Course title</div>
          <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Course title" />
        </label>

        <label style={{ display: "block", marginBottom: 12 }}>
          <div>PDF file</div>
          <input
            type="file"
            accept="application/pdf"
            onChange={(e) => setFile(e.target.files?.[0] || null)}
          />
        </label>

        <ModelProfileSelector value={modelProfileId} onChange={setModelProfileId} />

        <button type="submit" disabled={isSubmitting || !file}>
          Upload and process
        </button>
      </form>

      {error && <p style={{ color: "crimson" }}>{error}</p>}

      <LanguageConfirmationDialog
        open={Boolean(project?.languageConfirmationRequired)}
        detectedLanguage={project?.detectedLanguage || "en"}
        onConfirm={handleLanguageConfirm}
        onCancel={() => setProject(null)}
      />
    </main>
  );
}
