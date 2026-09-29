# Provenance and Evidence Boundary

## Classification

**Synthetic / internal benchmark. Not a client case.**

The displayed `Aster No. 01` perfume bottle is an invented benchmark product, not an existing commercial brand and not customer material.

The public proof is about the **web-delivery stage**. The raw GLB already existed before this stage; publishing it here does not claim that from-scratch modeling is part of the supported buyer responsibility.

## Original technical evidence

The source evidence was produced in a private technical benchmark workspace under the CPB-4 Web-ready GLB gate.

The accepted run preserved:

- raw GLB: `1,091,916 bytes`;
- accepted Meshopt GLB: `270,360 bytes`;
- 75.24% file-size reduction;
- 9/9 named product nodes;
- scene bounds;
- 28,544 upload vertices;
- material intent and required UV attributes;
- 0 validator errors / 0 warnings;
- real browser load in the pinned viewer stack;
- manually accepted raw/optimized visual equivalence.

The earlier 181,616-byte candidate was retained as negative evidence because it was smaller and validator-clean but visually worse in the browser.

## Broader existing-asset hardening evidence

A separate WAH-01 benchmark using the public CC0 Khronos FlightHelmet asset also completed an evidence-driven existing-asset hardening loop covering structural diagnosis, texture-aware optimization, geometry-aware optimization, Meshopt/Draco trade-offs, deterministic browser QA, and manual visual acceptance.

That broader benchmark supports the workflow class, but its asset-specific percentages are not copied into this proof as promises.

## Private material intentionally excluded

Not published here:

- personal Runner / Local Execution Fabric implementation;
- browser-control infrastructure;
- credentials or session material;
- private orchestration/control-plane code;
- unrelated internal scripts and repositories;
- any claim that internal automation itself is the buyer product.

## Responsibility boundary

Supported:

> existing usable GLB/glTF → inspect → bounded optimization → structural validation → target-browser QA → manual visual comparison → accepted delivery artifact + evidence.

Not supported by this proof:

- arbitrary source formats without inspection;
- arbitrary damaged models;
- major topology/UV/material reconstruction;
- animation/rigging;
- from-scratch or reference-to-product modeling;
- full production website/configurator integration;
- universal size-reduction guarantees.
