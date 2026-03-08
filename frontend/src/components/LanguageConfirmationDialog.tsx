import { useState } from "react";

type LanguageConfirmationDialogProps = {
  open: boolean;
  detectedLanguage: string;
  onConfirm: (language: string) => Promise<void>;
  onCancel: () => void;
};

export function LanguageConfirmationDialog({
  open,
  detectedLanguage,
  onConfirm,
  onCancel,
}: LanguageConfirmationDialogProps) {
  const [selectedLanguage, setSelectedLanguage] = useState(detectedLanguage || "en");
  const [saving, setSaving] = useState(false);

  if (!open) {
    return null;
  }

  const handleConfirm = async () => {
    setSaving(true);
    try {
      await onConfirm(selectedLanguage);
    } finally {
      setSaving(false);
    }
  };

  return (
    <div style={{ border: "1px solid #ccc", padding: 16, marginTop: 16 }}>
      <h3>Confirm document language</h3>
      <p>Detected language confidence is below 0.80. Confirm language to continue.</p>
      <select value={selectedLanguage} onChange={(e) => setSelectedLanguage(e.target.value)}>
        <option value="en">English</option>
        <option value="ru">Russian</option>
        <option value="uk">Ukrainian</option>
      </select>
      <div style={{ marginTop: 12, display: "flex", gap: 8 }}>
        <button type="button" onClick={handleConfirm} disabled={saving}>
          Confirm
        </button>
        <button type="button" onClick={onCancel} disabled={saving}>
          Cancel
        </button>
      </div>
    </div>
  );
}
