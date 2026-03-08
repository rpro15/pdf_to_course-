import { useState } from "react";

import { createExport, waitForExportReady } from "../services/exportService";

type ExportDownloadPanelProps = {
  projectId: string;
};

export function ExportDownloadPanel({ projectId }: ExportDownloadPanelProps) {
  const [status, setStatus] = useState<string>("idle");
  const [error, setError] = useState<string>("");

  const handleExport = async () => {
    setStatus("creating");
    setError("");
    try {
      const created = await createExport(projectId);
      const downloadUrl = await waitForExportReady(projectId, created.id);
      setStatus("ready");
      window.location.href = downloadUrl;
    } catch (err) {
      setStatus("error");
      setError(err instanceof Error ? err.message : "Export failed");
    }
  };

  return (
    <section style={{ marginTop: 20, borderTop: "1px solid #ddd", paddingTop: 12 }}>
      <h3>Export</h3>
      <button type="button" onClick={handleExport} disabled={status === "creating"}>
        Download to PC
      </button>
      <div style={{ marginTop: 6 }}>Status: {status}</div>
      {error && <div style={{ color: "crimson" }}>{error}</div>}
    </section>
  );
}
