**Geometry review — what the newest Docs can help with**

8 September 2026

Yes. The most useful additions are the resonator’s explicit G1 geometry, the toroidal all-orders memory argument, and the separately recorded L=3 validation follow-up. They connect to the existing project through a precise question: **what information must a description retain to support the particular measurement or prediction we want?**

This pass screened **71 retrieved files**: every result in the completed 54-file Geometry/Toroidal title search, plus 17 related files, including the newest Docs. Current definitions and relevant mathematical sections received focused review; older versions were screened for lineage. This was not a line-by-line certification of every historical theorem, a workbook audit, or a replay of the source simulation archives. The [source inventory](C:/Users/drewd/Documents/Codex/2026-09-08/che/outputs/geometry_source_inventory.md) records the coverage. The [independent arithmetic results](C:/Users/drewd/Documents/Codex/2026-09-08/che/outputs/geometry_checks.json) preserve the calculations performed in this review. No Docs or Drive files were changed.

**The new material at the top**

| Material | What it contributes | Assessment |
|---|---|---|
| [Five_String_Acoustic_Resonator_Rev_B — Geometry update G1](https://docs.google.com/document/d/1U05hPPHklm9yZBUcNHkLMYwDaUaaftbLBFkmeEbv_zQ/edit?tab=t.a4ezxd7jm5ha) | Actual coordinate conventions, a bar-envelope calculation, and a support footprint | Useful immediately for planning and measurement. Its displayed arithmetic checks out under its stated assumptions. |
| [The mathematical formulas shown across the images are-](https://docs.google.com/document/d/1Mw5r-NKLhq8eOoVnQVYOJ2pDJiDXsiiEnHww2QrwjEE/edit) | Eleven formula headings, including string tension, torque, cavity volume and Helmholtz frequency | The saved native document has blank paragraphs where the equations should be. A full native read found no embedded equations or image objects. Treat it as an incomplete checklist. |
| [Python prime](https://docs.google.com/document/d/1hQ8oTFRXjaJfHOSFlLslIlMAornoWbvIfdXEOetrwvM/edit) | A scripted prime/composite classification and resource-accounting demo | Potentially useful as a demonstration or a control with known rules. It does not test geometric closure: its outcomes are assigned by conditionals. |
| [Tesonator](https://docs.google.com/document/d/1x91qKvaEV-A4HALckCI6XxaUh4e2vCitXXPlJCiRuuk/edit) | Identifies revision and branding drift in a concept render; clarifies the intended public design | Useful for making future illustrations faithful to the engineering record. It supplies no new dimensions or measurements. |
| [thingy](https://docs.google.com/document/d/1Z_nWnPrHtuwZ9hqcNfT1xzwQRdBGnlmVqpQFyj65EBg/edit) and the recent transcripts | A recorded language switch and a proposed explanation | The transcript is usable observational evidence. The explanatory text does not establish the internal cause of the switch and adds no geometry result. |

The resonator’s first native tab is largely a conversation transcript; the actual new geometry is in its separate **Geometry update G1** tab. I also compared the prior task’s extracted Rev B engineering text and the accessible Rev A baseline. A title alone is not a reliable guide to which kind of record a file contains.

**What G1 actually fixes**

G1 assumes a literal 2 × 3 inch spine, five strings at 2-inch centres, and a 2-inch gap measured from the spine face. That gives string coordinates x = −4, −2, 0, 2, 4 inches and y = 3.5 inches.

With the stated one-inch radial allowance:

| Occupied geometry | Required clear circular diameter |
|---|---:|
| Outer string centre lines, 2-inch face gap | 12.6301 in |
| Assumed 10-inch bar, 0.5-inch thickness, 2-inch face gap | **14.5000 in** |
| Outer string centre lines, 3-inch face gap | 14.0416 in |
| Same assumed bar, 3-inch face gap | 15.7931 in |

The bar’s farthest assumed corner is (5, 3.75), whose radius is exactly 6.25 inches. Adding one inch gives a 7.25-inch radius. Thus **14.50 inches controls this example wherever the bar occupies the vessel**. Actual fittings, motion, vessel offset and the mouth profile must be included in the occupied envelope. This is not a universal vessel-size requirement for every possible layout.

G1 makes the existing Rev B fit correction more complete. Rev A’s blanket 12-inch clear-ID target cannot accommodate this example. The older eight-inch bar also provides only the eight-inch span between the outer hole centres, leaving no positive end allowance. [Rev A baseline](https://docs.google.com/document/d/1R3AjOu-f39DHhaLHhBfKhPbS-oh68BTJb6VakqIGnp4/edit)

The four point feet on a 14-inch circle give a support square 9.8995 inches across, with its nearest edge 4.9497 inches from the centre. With 1.5-inch-diameter feet and a 16-inch base, the nominal radial space outside a foot is 0.25 inch. Those numbers agree with G1; they describe geometry, not connection capacity or completed stability review.

One input mismatch needs attention when rebuilding the missing formula sheet: its heading names a **0.65 m** string example, whereas G1 retains **32 inches = 0.8128 m**. At fixed pitch and linear density, the latter needs **1.56365 times the ideal tension**, or 56.4% more. The two lengths must not share a tension calculation unchanged.

**A direct connection between the mathematics and the resonator**

For the ideal flexible-string model,

T = 4L²f²μ.

At fixed length, multiplying both tension T and mass per length μ by the same positive factor leaves the fundamental frequency f unchanged. This is a mathematical comparison, not an instruction to increase a physical string’s tension. [UNSW string acoustics](https://phys.unsw.edu.au/jw/strings.html)

Consequently, **pitch alone does not determine frame loading**. The observation “same pitch” merges states with different mechanical loads. Retaining the string identity or linear density repairs that specific loss of information.

That is a concrete physical use of [New geometry’s witness-descent test](https://docs.google.com/document/d/1DVgC8ia4Z1suHmLbcrDbvw1ETuSjkTm25_5DH8OOQNI/edit). It gives a reason for the string schedule, rather than merely adding paperwork.

Likewise, the simple Helmholtz formula depends on the ratio of opening area to cavity volume times effective neck length. Different geometries can share that ratio and the same approximate resonant frequency. End corrections and the suitability of the lumped model matter; the resonator’s open annulus is not automatically a textbook bottle neck. [UNSW Helmholtz resonance](https://phys.unsw.edu.au/jw/Helmholtz.html)

The productive acoustic comparison is therefore to retain **frequency, decay, excitation/reference level, sensor position and mounting**, then test which of those coordinates are necessary for reproducible response. This aligns with the recovered Rev B measurement plan. The [Chavín stress test](https://docs.google.com/document/d/1I_bpAt7J6NF6FgpYDTibkAnjNaTGrfDofVBVXk8ExaA/edit) supplies the same methodological lesson: broad frequency overlap was easy to obtain in its ideal duct family, whereas selective transmission was the more discriminating unresolved target.

**The toroidal work has advanced beyond the earlier review**

The [no-finite-Markov-order note](https://docs.google.com/document/d/1ON-nOrXUCCixHFm4WYIbihKtY47wQ2p0ylgR4r4opiY/edit) supplies an analytical argument for the ideal TD-COS-FH-001 kernel at J = 1, t = 1/2, zero charge-six source, unbounded integer currents, and each cubic size L ≥ 2. Its conclusion covers every fixed positive integer interval between attempted updates, including saved sweeps.

The key step is stronger than finding two hidden states with different predictions. Reversibility turns any finite-order sector law into the necessary identity A²u = cAu for the operator that retains all-zero sampled sectors. The uniform large-current states then violate this identity through a nonzero Bessel-tail correction. I checked that logical chain against the stated kernel and found no flaw in the core argument under its assumptions. The Bessel series used is consistent with [NIST DLMF 10.25.2](https://dlmf.nist.gov/10.25.E2); finite-order terminology is consistent with [Geiger and Temmel](https://arxiv.org/html/1212.4375v6).

I independently recomputed the six displayed return probabilities and derivatives, using exact rational convolution and the character formula. Both methods agree exactly. This corroborates the arithmetic; it is not proof-assistant verification or external mathematical review.

The practical consequence is that a fixed finite sector-history window cannot provide an exact autonomous predictor for that ideal model. **The useful next question is approximation quality at a declared horizon and error tolerance**, or a sufficient retained state/filter. The theorem does not rule out every finite-dimensional hidden-state description and does not quantify typical equilibrium memory.

There is also a reproducibility defect: the saved Doc promises a complete embedded verifier, but its code ends at **“assert a”** inside a function. The proof text is present; the advertised self-contained executable is incomplete. Recover the original full verifier before describing that Doc itself as independently runnable.

The [L=3 direct-reference follow-up](https://docs.google.com/document/d/1YNIuAhjiY9szcA9Q5uvMm0N-b88KEQ15jjzFRLvdanY/edit) changes a separate status. It reports 320,000 retained direct sweeps, a rarest holonomy count of **104 against the unchanged minimum of 100**, and passing comparison screens against the preserved dual cohort. I independently checked that its eight aggregate counts sum to 320,000 and reproduce its displayed Fourier reference probabilities.

This supports carrying forward the document’s **follow-up-supported engineering PASS**. The original pilot’s 33-count result remains unresolved. The separate [accepted-update mismatch investigation](https://docs.google.com/document/d/1G88zvSUXi78R6uCMJYBEZpOmFpIiyP8OAK8_gtd9Hxw/edit) remains unresolved, and the physical Q2 experiment remains unrun. I did not rerun these samplers.

**What carries forward from the rest**

| Branch | Useful contribution |
|---|---|
| [Geometry Maximization v2](https://docs.google.com/document/d/1Cn00U9Cj37QRrK2Xg3bX1417xYKstkFzednitR9xjog/edit) | The solved 39-screen remains the calibration model. My exact arithmetic check recovered 1,034 slips in 10,000 departures from phase zero. |
| [Recovered §35 comparison](https://docs.google.com/document/d/11nZWX9optKPLn9PX90cNktrj84iyafFNi3Pj1LDFZEk/edit) | Keep the normalized smooth-phase algebra. Its associator is −fgD²u; phase averaging and the noncommutative extension have different obstructions. I checked these definitions against §35 in the v1.6 receipt. |
| [Toroidal Geometry v1](https://docs.google.com/document/d/1NV7JsFuqJJVjFzYcqCAuC22y_rrjCSqqcZWZKobcGoU/edit) | Retain cut flux rather than substituting a volume average. The curved-throat velocity needs its metric correction; material and fixed-radius control tubes retain different flux witnesses. |
| [Reflex Geometry v3](https://docs.google.com/document/d/1C63lzqzNJZyMOvsXluJ0-kpNY4UIM_3RTOmaMEn5NuE/edit) | Equal output can conceal different resource use, correction compliance and capacity to continue. It also corrects the older energy/entropy bookkeeping and compulsory-mediator language. |
| [Amended holding-posture audit](https://docs.google.com/document/d/1uhM6kxWGuYBtKPLnSIXEEwUnL21R7aIbnLCCiu8we8k/edit) | Retain observable recurrence and correction outcomes. The record does not identify their upstream mechanism. |
| [Institutional comparison](https://docs.google.com/document/d/1h-4t4lFub9YIm-BSbKY1esdbBaeIucRKx3KldoIQ7lk/edit) | Preserve authority, chronology, coverage and successors separately; the geometry changed zero of five controlling case verdicts. |
| [NEO quotient-split record](https://docs.google.com/document/d/1EfT7lGNdhis8AQsR0_WkT0VDwkluv2Bu-rYDhkOjIi4/edit) | Directional similarity, encounter similarity and composition are different claims. No new astronomical factual verification was performed here. |
| [Tektite pairing audit](https://docs.google.com/document/d/1qdShAyYq0JRudfOmkB5-hK83JFSVy8ItfhCh5ThZTT0/edit) | Provides a concrete chemistry-versus-structure prediction design, but its required matched-specimen dataset was not verified and the comparison remains unrun. |
| [Atomic-number bridge](https://docs.google.com/document/d/1jEf1CAGO0ujtThcf1YX10f-4CuEhWzwT4JJJurNCoH8/edit) | The declared symmetry supports degree-six terms; its phase-averaged indexing found no prime-number preference. This gives no independent support to the new prime script’s assigned rules. |

The new prime script labels a sector by primality, calls that label “parity,” and returns closure statuses from the numeric value of a hash. Neither operation compares successor laws inside a shared observed state. As saved, it also needs constructor, entry-point and indentation repairs. Repairing syntax alone would not turn the scripted premise into a discovered result.

The older room sketches, emergence essays and abundance diagrams can inform design language or proposed comparisons. A diagram without dimensions, a defined update or observations cannot establish a physical mode, geometric closure or hidden mechanism. Current formal results should be carried through their explicit definitions rather than through shared terminology.

**Recommended next use**

1. Use G1 to collect the actual vessel profile and complete string/hardware envelope. Rebuild the formula sheet with declared units and one configuration’s dimensions.
2. Use the resonator to compare which measurements preserve load and acoustic response: pitch alone, then pitch plus string properties, then decay and transfer information.
3. Update the working research summary to include the all-orders toroidal argument and the separate L=3 follow-up status. Recover the truncated verifier before claiming a runnable package.
4. For further toroidal computation, define the prediction horizon, allowed error and state-distribution coverage before comparing finite history with a hidden-state filter.

These are practical extensions of the existing geometry. The strongest immediate result is **same measured pitch can hide different load**, which makes the information-retention method directly useful to the resonator.
