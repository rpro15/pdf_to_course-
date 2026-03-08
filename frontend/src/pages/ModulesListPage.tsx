import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

import { ExportDownloadPanel } from "../components/ExportDownloadPanel";
import { apiRequest } from "../services/apiClient";

type ModuleItem = {
  id: string;
  moduleIndex: number;
  title: string;
  summaryText: string;
  qualityScore: number;
  reviewRequired: boolean;
};

export function ModulesListPage() {
  const { projectId = "" } = useParams();
  const [modules, setModules] = useState<ModuleItem[]>([]);
  const [error, setError] = useState("");

  const loadModules = async () => {
    try {
      const data = await apiRequest<ModuleItem[]>(`/projects/${projectId}/modules`);
      setModules(data);
      setError("");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load modules");
    }
  };

  useEffect(() => {
    if (projectId) {
      loadModules();
    }
  }, [projectId]);

  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: 20 }}>
      <h1>Course modules</h1>
      <button type="button" onClick={loadModules}>
        Refresh
      </button>
      {error && <p style={{ color: "crimson" }}>{error}</p>}

      <ul>
        {modules.map((module) => (
          <li key={module.id} style={{ marginTop: 12 }}>
            <Link to={`/projects/${projectId}/modules/${module.id}`}>
              Module {module.moduleIndex}: {module.title}
            </Link>
            <div>Quality score: {module.qualityScore}</div>
            {module.reviewRequired && <div style={{ color: "darkorange" }}>Review required</div>}
          </li>
        ))}
      </ul>

      {projectId && <ExportDownloadPanel projectId={projectId} />}
    </main>
  );
}
