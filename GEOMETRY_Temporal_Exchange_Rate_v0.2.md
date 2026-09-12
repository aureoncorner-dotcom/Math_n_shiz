# Temporal exchange rate
## Working increment v0.2 — 12 September 2026
CC0 • Anonymous

Successor to v0.1. Adds: Normoyle vs Claypool operator split; jitter-buffer target rules; P.863 / P.863.1 as a voice-only secondary witness; BCI/TBW kept off the primary clock.
Status: hypothesis card. Attaches to Working Master v2.1, Typed Defects v0.2, Upgrade v2.2.
Does not alter: chemistry freeze, Hidden Quotient v1.7, 39-screen, TD-COS-FH-001, Kind VI.

---

## 0 Claim

**Temporal exchange rate.** When a system is already fast, a unit of timing irregularity costs more, on a declared user witness \(W\), than a unit of extra mean delay. A representation map that raises mean delay a little in order to cut variance — or that installs a *deterministic* duration-to-effector code — can therefore improve \(W\).

Interaction, not a main-effect slogan.

| Symbol | Meaning |
|---|---|
| \(\mu\) | mean action-to-usable-update latency on a declared clock |
| \(\sigma\) | declared irregularity (SD, jitter amplitude, interrupt rate, or number of distinct SRTs) |
| \(\Delta\) | pre-registered extra mean you are willing to spend |
| Region | low \(\mu\) |

**Fail.** A factorial in \((\mu,\sigma)\) has no low-\(\mu\) cell where raising \(\sigma\) hurts primary \(W\) more than raising \(\mu\) by \(\Delta\).

The phrase is not in the sources checked. Related interactions are. Novelty, if any: named tradeoff, named operator, fail region. Not “jitter exists.”

v0.1 treated “Claypool-style platform jitter” as one object. That was sloppy. v0.2 splits it.

---

## 1 Identification table

| Object | Role | Do not call it |
|---|---|---|
| \(\mu\) | mean on the declared clock | recovered specified output “the system is fast” |
| \(\sigma\) | irregularity on the same clock | TBW width; eta; MOS-LQO |
| Weber 2013 pad | lift short SRTs; *when* | BCI |
| Metronome | one duration; *when* | a *which*-cue |
| Thomaschke deterministic map | duration \(\leftrightarrow\) effector; *which* | smoothing |
| 0.8 map | noisy *which* | “pretty deterministic” |
| Normoyle et al. 2014 | *damage*: inject \(\sigma\) on a platformer clock | Claypool; a pad |
| Claypool buffer | *intervention*: queue, emit smoother, pay \(\mu\) | Normoyle; time warp |
| NetEQ / percentile target | live high-percentile \(T(t)\) plus stretch | a TBW |
| P.863 MOS-LQO | listening quality of a speech pair | interactivity; game feel |
| TBW | SOA contour for two cues | theory of padding |
| BCI \(p(C=1)\) | one source vs two | descent through \(\pi\) |
| Intentional binding | judged action–outcome compression | TBW |
| \(\pi_{\mathrm{DS}}\) | served object + answer | a latency law |

---

## 2 Related measurements

**Normoyle, Guerrero, Jörg (SAP 2014).** Platformer. Constant delay vs delay-plus-jitter applied independently to character pose. Constant \(\mu\) to ~300 ms often left experience intact. \(\mu=200\) ms plus jitter: noticed more, blocked practice, more goal failures, worse motion quality. This is a **damage operator**, not a pad.

**TAP 2025 (target acquisition).** Mean × jitter amplitude. Jitter hurt completion time a little; that hurt *shrank as mean rose*. Mean carried most of the impairment. Exchange-rate *shape*, mean still bigger.

**Schmid, Halbhuber et al.** FPS, ±50 ms on 50 vs 150 ms base: no performance effect. Small-amplitude null. Do not test only this cell and declare victory or death.

**Weber, Haering, Thomaschke (2013).** Sequential GUI. Short SRTs lengthened; mean SRT up; user RTs down; UX ratings not worse. This is the **pad intervention** on an office clock.

**Thomaschke & Haering (2014).** Constant beats variable non-predictive *and* beats 0.8 predictivity. Deterministic duration-to-target beats constant.

**Thomaschke & Dreisbach (2013).** In speeded two-choice, the duration map paid off when it named the **effector**, not the stimulus or an abstract goal. Foreperiod / CNV / LRP: *when* vs *which finger* are different preparations.

**Claypool line.** Precision × deadline classifies which actions die at modest \(\mu\). Latency-compensation taxonomy (prediction, time warp) is a different map. Playout / jitter buffers in that family implement the pad on streams: E-policy can kill interrupts and lose QoE when extra delay dominates; queue-monitoring with decay balances. Do not cite Claypool as the SAP 2014 platform result.

**TBW / BCI.** Binding window = SOA band where two sensory events fuse or are judged simultaneous. BCI = prior \(p_c\) on one cause vs two, then average / select / match. Window = posterior contour. Use only if the user must bind two streams. Intentional binding is another compression.

**Queueing variance → delay** is a production claim, not UX support.

---

## 3 Operators (name one before the run)

**Damage (Normoyle).** Add \(\sigma\) at fixed \(\mu\). Measures the tax. Does not test the intervention.

**Variance kill / pad (Weber 2013; fixed jitter buffer).** Lift shorts to a ceiling or to p95. \(\mu\uparrow\), \(\sigma\downarrow\).

**Metronome.** One duration.

**Signal pad.** Duration is 1–1 for the next effector or stable response class. Not smoothing.

**Adaptive buffer (NetEQ-class).** Target \(T(t)\) from a live histogram of relative delay (high percentile, forget factor, underrun + reorder terms). Each tick: normal / accelerate / preemptive-expand / PLC-expand / merge. Report \(T(t)\), realized \(\mu\), remaining interrupts, stretch fraction.

**Occupancy buffer (QM / E-policy).** Steer queue length. E-policy spends \(\mu\) to avoid stalls; QM/decay will drop frames to cap \(\mu\).

0.8 maps are a confound.

---

## 4 Witnesses

Declare, in order: \(D\); clock (action onset → first usable update); \(W_\mu\), \(W_\sigma\); **one** primary user \(W\); stream \(U\); D5 question (does equal retained mean imply equal next-action law?).

**D1.** \(N_{(W_\mu,W_\sigma)}=N_\mu\cup N_\sigma\).

**D2 / Kind I.** “Fast on average” can descend while “next gap is usable” does not.

**D5.** Next-action law may depend on the realized gap.

**D4.** Pointing ≠ FPS ≠ GUI SRT ≠ token stream ≠ voice.

Padding is a representation map on the served clock (v2.1). Score \(A_{\mathrm{task}}\) separately from \(A_{\mathrm{sel}}\). Versioning certifies protocol, not \(W_\sigma\).

### Voice-only secondary: P.863

If \(D\) is speech and the operator warps or conceals audio, MOS-LQO (P.863 Ed. 3) may be a **secondary** witness for listening damage. Protocol freeze is P.863.1: FB vs NB mode (do not mix scales), reference ≥3 s and ≤6 s active, ≤12 s total, −26 dBov, 16-bit PCM, paired files, declared tap, no silent peak-normalize. Cap ~4.5 NB / ~4.8 FB. Constant delay without waveform warp is mostly invisible to MOS-LQO. Conversational delay is out of scope. MOS-LQO up and primary \(W\) down is an exchange-rate datum, not a win.

---

## 5 Factorial

| | Low \(\sigma\) | High \(\sigma\) |
|---|---|---|
| Low \(\mu\) | fast + smooth | variance-dominates candidate |
| High \(\mu\) | delay-dominates | both-bad |

**Support.** \((\mu_{\mathrm{low}}+\Delta,\,\sigma_{\mathrm{low}})\) beats \((\mu_{\mathrm{low}},\,\sigma_{\mathrm{high}})\) on primary \(W\). Name \(\Delta\) (example: +30 ms vs jitter in the TAP ~67 ms amplitude band, not only ±50 ms).

**Fail.** No such low-\(\mu\) region. “Interaction, mean still wins” (TAP) is a weak fail if the paper claimed variance *outranks* mean; a survive if the paper claimed only a nonzero interaction. Write that sentence first.

Jitter **amplitude**, not frequency, unless frequency is the claim.

Twelve adversarial reviews ≠ twelve external reviews.

---

## 6 What v0.2 adds over v0.1

1. Normoyle damage ≠ Claypool buffer ≠ Weber pad ≠ Thomaschke signal.
2. Adaptive / occupancy buffers as named implementations of the pad, with what to log.
3. P.863.1 as a protocol-frozen secondary \(W\) for voice, explicitly not the primary.
4. Same fail region.

Still not established: the interaction on any \(D\) in this card; a shape of \(N_W\); transfer across domains.

\[
\boxed{\text{CLAIM + OPERATORS + FALSIFIER: STATED}}
\]
\[
\boxed{\text{EMPIRICAL INTERACTION: NOT RUN HERE}}
\]
\[
\boxed{\text{SOURCE FREEZES: UNCHANGED}}
\]

---

## 7 Use

One \(D\), one primary \(W\), one operator, named \(\Delta\). Do not promote a coefficient that separates one pair into a global recovery theorem.
