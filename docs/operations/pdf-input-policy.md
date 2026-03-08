# PDF Input Policy (MVP)

## Supported Input
- Text-based PDF documents are supported.
- Typical expected input is multi-chapter educational content.

## Unsupported Input
- Image-only/scanned PDFs are not supported in MVP.
- Password-protected PDFs are treated as unsupported.

## Runtime Behavior
- The upload endpoint validates source type before processing.
- If source is image-only, project processing is rejected with an explicit error.
- Artifacts are stored for up to 24 hours, then removed automatically.
