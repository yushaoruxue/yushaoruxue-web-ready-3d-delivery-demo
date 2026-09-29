# Publication Gate

## Standalone repository

`yushaoruxue-web-ready-3d-delivery-demo`

## Current status

**PUBLIC / BUYER-SENDABLE — publication verification pending only on current CI run.**

Publication surface now contains:

- public buyer-facing README;
- real raw and accepted browser screenshots;
- downloadable accepted web-ready GLB;
- frozen source-baseline size/hash metadata;
- acceptance and provenance evidence;
- reproducible 10-check integrity test.

Required final checks:

1. repository visibility is public;
2. root README renders without authentication;
3. raw and optimized browser screenshots render;
4. accepted optimized GLB is downloadable;
5. acceptance/provenance files are publicly readable;
6. `python tests/verify_evidence.py` reports `10/10 evidence checks PASS`;
7. no private execution infrastructure, local build path, credential, session, or private repository implementation is exposed;
8. the synthetic/internal label and current responsibility boundary are visible;
9. the public URL is written back to the commercial proof registry.

The source GLB itself is not duplicated into the public proof; its exact size/hash and browser baseline are preserved, while the accepted delivery GLB is published directly.
