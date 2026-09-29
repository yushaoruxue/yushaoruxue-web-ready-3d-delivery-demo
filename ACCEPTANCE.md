# Acceptance Evidence

> Synthetic benchmark acceptance. This is not client acceptance.

## Frozen delivery gate

The accepted web-ready candidate had to satisfy all of the following:

1. The source GLB remains available as the compatibility baseline.
2. The optimized file is materially smaller than the source.
3. No geometry deletion is introduced by the accepted path.
4. All 9 expected product node names remain present.
5. Scene bounds remain unchanged.
6. Upload vertex count remains unchanged at 28,544.
7. Generic validator reports 0 errors and 0 warnings.
8. The target browser/viewer actually loads the Meshopt-compressed asset.
9. Browser capture reaches the ready state without a model error.
10. Manual side-by-side review finds no unacceptable regression in cap reflections, glass, liquid, label/text, or visible geometry.

## Current accepted result

**PASS**

- raw: `1,091,916 bytes`
- accepted optimized: `270,360 bytes`
- reduction: `75.24%`
- size ratio: `4.04×`
- expected product nodes: `9/9 preserved`
- validator: `0 errors / 0 warnings`
- browser load: `PASS`
- manual visual review: `PASS`

Supporting pixel comparison, excluding the status-label area:

- mean absolute channel difference: approximately `0.034 / 255`;
- RMSE: approximately `0.468 / 255`;
- pixels with any channel difference `> 8/255`: approximately `0.072%`.

## Rejected smaller candidate

A previous candidate reached `181,616 bytes` and was validator-clean, but browser review showed the polished cap becoming materially flatter/greyer after UV attributes were removed.

That candidate was rejected.

This is an intentional part of the proof: **machine-clean + smaller is insufficient when the agreed visual/runtime result regresses.**

## Runtime boundary

The accepted optimized GLB requires:

- `EXT_meshopt_compression`;
- `KHR_mesh_quantization`;
- compatible Meshopt decoding in the target viewer/runtime.

The generic validator used in the benchmark reports the Meshopt extension as unsupported for extension-specific validation. Therefore acceptance was not inferred from validator output alone; actual browser decode/load and visual comparison were required.
