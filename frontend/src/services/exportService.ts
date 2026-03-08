import { API_BASE_URL, apiRequest } from "./apiClient";

export type ExportPayload = {
  id: string;
  status: string;
  format: string;
  files: string[];
  storagePath: string;
};

export async function createExport(projectId: string): Promise<ExportPayload> {
  return apiRequest<ExportPayload>(`/projects/${projectId}/exports`, {
    method: "POST",
  });
}

export function getDownloadUrl(projectId: string, exportId: string): string {
  return `${API_BASE_URL}/projects/${projectId}/exports/${exportId}/download`;
}

export async function waitForExportReady(
  projectId: string,
  exportId: string,
  attempts = 8,
  delayMs = 1000,
): Promise<string> {
  const url = getDownloadUrl(projectId, exportId);
  for (let i = 0; i < attempts; i += 1) {
    const response = await fetch(url, { method: "HEAD" });
    if (response.ok) {
      return url;
    }
    await new Promise((resolve) => setTimeout(resolve, delayMs));
  }
  throw new Error("Export package is not ready");
}
