import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { UploadProcessPage } from "./UploadProcessPage";
import { ModulesListPage } from "./ModulesListPage";
import { ModuleEditorPage } from "./ModuleEditorPage";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<UploadProcessPage />} />
        <Route path="/projects/:projectId/modules" element={<ModulesListPage />} />
        <Route path="/projects/:projectId/modules/:moduleId" element={<ModuleEditorPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
