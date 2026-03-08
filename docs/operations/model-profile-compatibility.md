# Model Profile Compatibility and Rollback

## Profile Snapshot
- Every processing run stores model profile identity and prompt version snapshot.
- Snapshot allows deterministic tracing of generated module/question outputs.

## Compatibility Rule
- If current profile metadata differs from the run snapshot, processing result is marked for compatibility review.
- Existing artifacts remain downloadable until TTL expiration.

## Rollback
- Rollback manager can restore prior profile metadata for future runs.
- Rollback does not mutate already generated module content.
