# Export and Download Contract

## Export Output
- One export action creates both `course.json` and `course.md`.
- Files are bundled into a single ZIP package.

## Download UX
- User clicks **Download to PC** on the modules page.
- Frontend triggers export creation and waits for package readiness.
- Browser starts ZIP download from the download endpoint.

## Retention
- Export artifact follows the same 24-hour retention policy as other project artifacts.
