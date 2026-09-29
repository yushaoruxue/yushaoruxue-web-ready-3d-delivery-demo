# Web-ready 3D Delivery Demo

> **Synthetic / internal proof — not a client case. The input asset already existed before this delivery stage.**

A compact proof for one bounded responsibility:

**existing GLB → diagnose → optimize → validate → load in a real browser → visually compare → deliver the accepted web asset**

## Result

| Source GLB | Accepted web-ready GLB |
| ---: | ---: |
| **1,091,916 bytes** | **270,360 bytes** |
| baseline | **75.24% smaller** |
| 0 validator errors / 0 warnings | 0 validator errors / 0 warnings |
| browser PASS | browser PASS |

The accepted file is **4.04× smaller** while preserving the benchmark's 9/9 named product nodes, scene bounds, upload vertex count, material intent, and browser-visible appearance.

<table>
<tr><th>Raw browser result</th><th>Accepted optimized browser result</th></tr>
<tr>
<td><img src="assets/raw-browser.jpg" alt="Raw GLB rendered in browser" width="360"></td>
<td><img src="assets/optimized-browser.jpg" alt="Optimized GLB rendered in browser" width="360"></td>
</tr>
</table>

## Why browser QA matters

A first optimization candidate reached **181,616 bytes** and also had no validator errors/warnings, but it was **rejected** because the polished metal cap became visibly flatter/greyer in the browser after UV attributes were removed.

<img src="assets/rejected-181kb-browser.jpg" alt="Rejected smaller candidate with visible cap-material regression" width="360">

So the delivery rule is not "make the file as small as possible." It is:

> **reduce cost without accepting a visible regression in the agreed target runtime.**

## Inspect it in under one minute

1. Compare the real raw and accepted browser captures above.
2. Compare the rejected smaller candidate.
3. Check the [acceptance evidence](ACCEPTANCE.md).
4. Inspect the frozen GLB size/hash evidence in [evidence/proof-manifest.json](evidence/proof-manifest.json).
5. Read the [responsibility boundary](#what-this-proves--and-what-it-does-not).

The binary GLBs are not duplicated into this buyer-facing repository. Their exact frozen byte sizes and SHA-256 hashes are retained as provenance evidence; this repository is an evidence surface, not a mirror of the private production workspace.

## What was done

The accepted path deliberately stayed narrow:

```text
existing raw GLB
→ inspect size / structure / materials
→ Meshopt high with bounded quantization
→ preserve UV attributes
→ validate
→ load with compatible Meshopt decoder
→ fixed-camera raw/optimized browser capture
→ manual visual comparison
→ accept
```

No prune, no simplify, no texture compression, and no geometry deletion were used in the accepted candidate.

The optimized file requires:

- `EXT_meshopt_compression`;
- `KHR_mesh_quantization`;
- a compatible Meshopt decoder in the target runtime.

That dependency is part of the delivery boundary, not hidden from the buyer.

## Acceptance evidence

For the accepted candidate:

- raw size: **1,091,916 bytes**;
- optimized size: **270,360 bytes**;
- reduction: **75.24%**;
- product nodes preserved: **9/9**;
- scene bounds preserved;
- upload vertices preserved: **28,544**;
- validator errors: **0**;
- validator warnings: **0**;
- raw browser load: **PASS**;
- optimized browser load: **PASS**;
- optimized model error marker: **false**;
- manual visual review: **PASS**;
- measured raw-vs-optimized screenshot RMSE: approximately **0.468 / 255**;
- pixels with any channel difference > 8/255: approximately **0.072%**.

Pixel metrics are supporting evidence; visual acceptance remains the meaningful gate.

## What this proves — and what it does not

This proof supports a bounded first responsibility such as:

> Given an existing usable GLB/glTF asset and a known target viewer/runtime, inspect the asset, choose a compatible optimization path, produce a smaller delivery artifact, validate it, browser-test it, visually compare it with the source, reject regressions, and hand off the accepted file plus evidence.

It does **not** claim:

- a real client engagement;
- from-scratch 3D modeling;
- reference-image-to-model production;
- arbitrary damaged-asset repair;
- major retopology or UV reconstruction;
- animation or rigging;
- arbitrary FBX / OBJ / CAD support without inspection;
- a complete Three.js configurator;
- Shopify/ecommerce integration;
- production CDN/deployment ownership;
- a guaranteed percentage reduction for arbitrary assets.

The **75.24%** reduction is benchmark evidence for this asset, not a universal promise.

## Reproduce the public evidence check

Python 3, standard library only:

```bash
python tests/verify_evidence.py
```

Expected final line:

```text
10/10 evidence checks PASS
```

This script verifies the public visual evidence bytes and the committed frozen acceptance metadata. It does not pretend to rerun the original GLB transform, browser session, or human visual review.

See [PROVENANCE.md](PROVENANCE.md) for the source-evidence boundary.
