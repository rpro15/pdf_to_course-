import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

import { QuestionEditorList } from "../components/QuestionEditorList";
import {
  applyOptimisticSavedState,
  createModuleEditorState,
  setDirty,
  setSaving,
  type ModuleEditorState,
  type ModulePayload,
} from "../state/moduleEditorState";
import { apiRequest } from "../services/apiClient";

export function ModuleEditorPage() {
  const { projectId = "", moduleId = "" } = useParams();
  const [state, setState] = useState<ModuleEditorState | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const load = async () => {
      try {
        const modules = await apiRequest<ModulePayload[]>(`/projects/${projectId}/modules`);
        const target = modules.find((module) => module.id === moduleId);
        if (!target) {
          setError("Module not found");
          return;
        }
        setState(createModuleEditorState(target));
        setError("");
      } catch (err) {
        setError(err instanceof Error ? err.message : "Failed to load module");
      }
    };

    if (projectId && moduleId) {
      load();
    }
  }, [projectId, moduleId]);

  const save = async () => {
    if (!state) {
      return;
    }

    setState((current) => (current ? setSaving(current, true) : current));
    setError("");

    const payload = {
      title: state.title,
      summaryText: state.summaryText,
      questions: state.questions,
    };

    try {
      const saved = await apiRequest<ModulePayload>(`/projects/${projectId}/modules/${moduleId}`, {
        method: "PATCH",
        body: JSON.stringify(payload),
      });
      setState((current) => (current ? applyOptimisticSavedState(current, saved) : current));
    } catch (err) {
      setState((current) => (current ? setSaving(current, false) : current));
      setError(err instanceof Error ? err.message : "Failed to save");
    }
  };

  if (!state) {
    return (
      <main style={{ padding: 20 }}>
        <Link to={`/projects/${projectId}/modules`}>Back to modules</Link>
        {error && <p style={{ color: "crimson" }}>{error}</p>}
      </main>
    );
  }

  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: 20 }}>
      <Link to={`/projects/${projectId}/modules`}>Back to modules</Link>
      <h1>Module editor</h1>

      <label style={{ display: "block", marginBottom: 12 }}>
        <div>Title</div>
        <input
          value={state.title}
          onChange={(e) =>
            setState((current) =>
              current ? setDirty({ ...current, title: e.target.value }) : current,
            )
          }
          style={{ width: "100%" }}
        />
      </label>

      <label style={{ display: "block", marginBottom: 12 }}>
        <div>Summary</div>
        <textarea
          value={state.summaryText}
          onChange={(e) =>
            setState((current) =>
              current ? setDirty({ ...current, summaryText: e.target.value }) : current,
            )
          }
          rows={12}
          style={{ width: "100%" }}
        />
      </label>

      <QuestionEditorList
        questions={state.questions}
        onChange={(questions) =>
          setState((current) => (current ? setDirty({ ...current, questions }) : current))
        }
      />

      <div style={{ marginTop: 12 }}>
        <button type="button" onClick={save} disabled={state.isSaving || !state.isDirty}>
          {state.isSaving ? "Saving..." : "Save"}
        </button>
      </div>

      {error && <p style={{ color: "crimson" }}>{error}</p>}
    </main>
  );
}
