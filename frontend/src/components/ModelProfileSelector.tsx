type ModelProfileSelectorProps = {
  value: string;
  onChange: (value: string) => void;
};

const MODEL_PROFILES = [
  { id: "00000000-0000-0000-0000-000000000001", label: "Default" },
  { id: "education-en-v1", label: "Education EN" },
  { id: "education-ru-v1", label: "Education RU" },
];

export function ModelProfileSelector({ value, onChange }: ModelProfileSelectorProps) {
  return (
    <label style={{ display: "block", marginBottom: 12 }}>
      <div>Model profile</div>
      <select value={value} onChange={(e) => onChange(e.target.value)}>
        {MODEL_PROFILES.map((profile) => (
          <option key={profile.id} value={profile.id}>
            {profile.label}
          </option>
        ))}
      </select>
    </label>
  );
}
