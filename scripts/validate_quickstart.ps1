$ErrorActionPreference = 'Stop'

Write-Host "Validating quickstart prerequisites..."

$requiredFiles = @(
  "backend/pyproject.toml",
  "frontend/package.json",
  "infra/docker/docker-compose.yml",
  "specs/001-pdf-course-mvp/quickstart.md"
)

$missing = @()
foreach ($file in $requiredFiles) {
  if (-not (Test-Path $file)) {
    $missing += $file
  }
}

if ($missing.Count -gt 0) {
  Write-Error ("Quickstart validation failed. Missing files: " + ($missing -join ", "))
  exit 1
}

Write-Host "Quickstart validation passed."
