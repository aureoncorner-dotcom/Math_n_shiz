# GQG Core Card · v0.3

## Retained Context, Conditioning, Descent, and Realization

**Status:** experimental language specification  
**Profile:** `Set` (normative core)  
**Date:** 2026-08-26  
**Attribution:** family-built  
**License:** CC0 — Public Domain — No rights reserved  
**Continuity:** conservative extension of GQG Core Card v0.2  
**Purpose:** a typed visual and textual language for witness-relative quotients, retained context, conditioned sources, quotient transport, and reproducible realizations

> **Claim boundary.** GQG records observations, the equivalence they induce, the quotient they justify, retained context, conditioning, and the proof obligations required for later transport. It does not claim that different application domains are isomorphic, that measurement is automatically quotienting, that conditioning is quotienting, or that a shared Hamiltonian governs those domains.

## v0.3 governing correction

An ordinary quotient is determined by its source and declared equivalence relation. It is therefore too strong to say that every quotient is additionally *defined* by retained data.

The precise upgrade is:

> **An observational specification is not exhausted by its quotient object. It also records the witness, any retained context or conditioning, and the realization through which a claim is produced.**

This keeps the mathematics of quotients intact while giving retained seams, boundary sectors, holonomies, normalizations, and computational provenance a typed home.

## Semantic ownership

**Text source → canonical AST → type checker → formal outputs**  
**Canonical AST → glyph, diagram, accessible-text, and canonical-record renderings**

The abstract syntax tree owns the semantics. A rune, commutative diagram, monochrome view, terminal view, and canonical JSON may all render the same accepted tree. Diagram-to-AST parsing remains a future feature and must pass semantic round-trip tests before the arrow becomes bidirectional.

A semantic witness specification and a computational execution are different objects:

```text
WitnessSpec = (profile, source, context, witness, observation,
               equivalence, quotient, claim rule)

Execution   = (WitnessSpec identifier, algorithm, code, parameters,
               seeds, selection rule, data, environment, manifest)
```

An execution realizes a witness specification. It does not define the mathematical witness merely by having a hash.

## Canonical constructions

### Base quotient

`CAT → SRC → WIT → OBS → EQV → QUO → (IMG) → {DSC, REF, (CPL)}`

In the normative `Set` profile, for a witness family $W$,

$$
O_W:=\prod_{w\in W}O_w,
\qquad
\Omega_W:P\to O_W,
\qquad
\Omega_W(x):=(w(x))_{w\in W}.
$$

Define

$$
x\sim_W y
\iff
\Omega_W(x)=\Omega_W(y).
$$

Then

$$
P\xrightarrow{q_W}Q_W:=P/{\sim_W}
\cong
\operatorname{im}(\Omega_W)
\hookrightarrow
O_W.
$$

The quotient–image comparison is conditional in other backends: the profile must declare the needed products, kernel pairs, coequalizers, images, and exactness assumptions.

### Retained context

Declare a context map

$$
r:P\to S.
$$

Retaining $r$ means refining the observation:

$$
\Omega_{W\oplus r}
:=
\langle\Omega_W,r\rangle
:
P\to O_W\times S.
$$

Thus

$$
x\sim_{W\oplus r}y
\iff
x\sim_W y
\text{ and }
r(x)=r(y).
$$

Equivalently, the map

$$
x\longmapsto\bigl([x]_W,r(x)\bigr)
$$

has kernel pair $\sim_{W\oplus r}$. Its image is a realization of $Q_{W\oplus r}$; it is not, in general, a map defined on $Q_W$.

Since

$$
\sim_{W\oplus r}\;\subseteq\;\sim_W,
$$

there is a canonical comparison

$$
Q_{W\oplus r}\twoheadrightarrow Q_W.
$$

Retaining context therefore produces a finer observational quotient. If $r$ is already constant on every $W$-class, the refinement is redundant and the comparison is an isomorphism.

### Conditioning

For a declared value $s\in S$, define the context fiber

$$
P_s:=r^{-1}(s).
$$

The conditioned witness is the restriction

$$
\Omega_{W\mid s}:=\Omega_W|_{P_s},
$$

with

$$
x\sim_{W\mid s}y
\iff
x,y\in P_s
\text{ and }
\Omega_W(x)=\Omega_W(y).
$$

The conditioned quotient is

$$
Q_{W\mid s}:=P_s/{\sim_{W\mid s}}.
$$

Surface notation such as $x\equiv_{W\mid r=s}y$ may be rendered for emphasis, but its canonical AST node is the observation-lane relation $\sim_{W\mid s}$. Conditioning does not create a new equality lane.

### When conditioning descends

The context $r$ descends through $q_W$ exactly when it is constant on witness classes:

$$
x\sim_W y
\Longrightarrow
r(x)=r(y).
$$

Under this condition there is a unique map

$$
\bar r:Q_W\to S
$$

such that

$$
r=\bar r\circ q_W.
$$

Only then is “condition after quotient” canonically defined, and in `Set` one obtains

$$
Q_{W\mid s}
\cong
\bar r^{-1}(s).
$$

If the condition fails, $C_{\bar r}Q_W$ is not merely known to differ from $Q_WC_r$: the post-quotient expression is undefined because no $\bar r$ exists.

## Token alphabet

| Token | Typed role |
|---|---|
| `CAT` | Ambient category or structural profile |
| `SRC` | Presented source object $P$ |
| `CTX` | Declared context map $r:P\to S$ |
| `COND` | Source restriction to a declared fiber $P_s=r^{-1}(s)$ |
| `WIT` | Witness family $W$ on its declared source |
| `OBS` | Aggregate observation $\Omega_W:P\to O_W$ |
| `RET` | Retained-context refinement $\Omega_{W\oplus r}=\langle\Omega_W,r\rangle$ |
| `EQV` | Kernel pair / induced equivalence $\sim_W$ |
| `QUO` | Quotient object and map $q_W:P\twoheadrightarrow Q_W$ |
| `IMG` | Backend-supported image factorization |
| `DSC` | Certificate that a map, operation, or context descends |
| `REF` | Witness refinement and quotient comparison |
| `REAL` | Computational realization and execution manifest |
| `CPL` | Separately typed completion specification |

## Equality lanes

| Lane | Form | Meaning |
|---|---|---|
| Source | $x=y$ | The presented elements are equal. |
| Observation | $x\sim_Wy$, including $x\sim_{W\mid s}y$ | The declared witness architecture cannot distinguish them. |
| Quotient | $[x]_W=[y]_W$ | They name the same quotient class. |
| Completion | $u=v$ in $\widehat Q_W$ | Equality may involve new completion elements; the declared embedding must state what it preserves and reflects. |

Never move a claim between lanes without an explicit constructor or proof. Retention and conditioning refine the observation lane; they do not authorize source equality.

## Formation rules

1. Declare `CAT` before `SRC`; v0.3 accepts only the explicit normative declaration `category Set`.
2. Every `WIT` names its source, and every `OBS` has a complete domain and codomain.
3. For an arbitrary map, `EQV` means the kernel pair—not an algebraic kernel.
4. Form `QUO` only when the active profile supports the required quotient.
5. Emit `IMG` and $Q_W\cong\operatorname{im}(\Omega_W)$ only when the backend justifies that factorization.
6. Defining an operation on $Q_W$ induced by a source operation requires `DSC`: if each $x_i\sim_Wy_i$, then $f(x_1,\ldots,x_n)\sim_Wf(y_1,\ldots,y_n)$. The certificate must reference a checked proof term or an externally verified obligation.
7. A finer witness system induces a finer quotient, and that finer quotient maps canonically onto the coarser quotient; the quotient arrow points fine → coarse.
8. `CPL` must name its added structure—for example, metric, order, topology, or norm. `Set` alone cannot justify a Dedekind completion.
9. Every `CTX` declares its domain, codomain, and semantic role. Mere metadata is not automatically a context map.
10. `RET[W,r]` constructs $W\oplus r$. It must not be rendered as though $r$ were already a function on $Q_W$.
11. `COND[r=s]` constructs the fiber source $P_s$ before forming its witness quotient.
12. Post-quotient conditioning requires a checked context-descent certificate. Without it, the expression is ill-typed.
13. Any change of source, boundary conditions, context, gauge choice, sector, witness, observation, normalization, projection, claim rule, or realization must be declared at the layer where it acts.
14. Transport from $(P,W)$ to $(P',W')$ through $T:P\to P'$ requires

    $$
    x\sim_Wy
    \Longrightarrow
    T(x)\sim_{W'}T(y).
    $$

    Only then does a unique $\bar T:Q_W\to Q_{W'}$ exist with

    $$
    q_{W'}\circ T=\bar T\circ q_W.
    $$

15. `REAL` must reference a semantic witness specification. A digest can establish byte identity and lineage; it does not establish semantic correctness, physical validity, or evidentiary independence.
16. Weighted marginalization, partition-function summation, and probabilistic renormalization are not `Set` quotients. They require a future weighted/probabilistic backend or an external theorem certificate.

## No Silent Architecture Change

$$
\boxed{
W\longrightarrow W'
\text{ requires a declared map and, for quotient transport, a descent certificate.}
}
$$

More generally, a change may act on `SRC`, `CTX`, `WIT`, `OBS`, `QUO`, the claim rule, or `REAL`. The checker must record which layer changed. Reusing the same observable name does not prove that the witness architecture stayed fixed.

The governing square is

$$
\begin{array}{ccc}
P & \xrightarrow{q_W} & Q_W \\
{\scriptstyle T}\downarrow & & \downarrow{\scriptstyle\bar T} \\
P' & \xrightarrow{q_{W'}} & Q_{W'}
\end{array}
$$

The desired quotient claim exists only when the square commutes.

## Non-Substitution and Conjunctive Promotion

Let separate witness architectures produce claims

$$
C_i=D_i(W_i),
\qquad i=1,\ldots,n.
$$

GQG permits the conjunction

$$
C_1\land\cdots\land C_n
$$

without permitting silent substitutions $C_i\Rightarrow C_j$. A stronger promoted claim $C$ requires a declared inference rule or certificate

$$
C_1,\ldots,C_n\vdash C.
$$

This is deliberately not called an “independence” rule. Statistical or evidentiary independence is an additional claim that must be proved. Algebraically equivalent diagnostics are implementation cross-checks, not independent witnesses merely because they have different names.

## Provenance and witness identity

The semantic identity of a witness is controlled by its checked specification. The historical identity of a run or artifact is controlled by its execution record.

| Question | Controlling record |
|---|---|
| What mathematical distinctions does the witness retain or erase? | `WitnessSpec` |
| Which code, parameters, data, seed, and selection rule produced this output? | `Execution` / `REAL` |
| Are two files byte-identical or linked by a frozen lineage? | Digest and provenance graph |
| Are two implementations semantically equivalent? | A refinement, equivalence, or transport certificate—not hashes alone |

Different digests may faithfully realize the same witness. One frozen digest may faithfully preserve a bug. Provenance is therefore necessary for reproducibility but insufficient for truth.

## Worked card

### Minimal source form

```text
category Set
source P = Integers

codomain ParityBits = Z/2Z
witness Parity on P {
  observation omega2 : P -> ParityBits
  definition omega2(n) = n mod 2
}

equivalence same_parity := kernel_pair(omega2)
quotient Q2 := P / same_parity

codomain Residues4 = Z/4Z
context Phase4 on P {
  map r4 : P -> Residues4
  definition r4(n) = n mod 4
}

retain Phase4 with Parity as ParityWithPhase4
condition Phase4 = 0 as P0

operation add : P × P -> P
certificate add_respects_parity {
  require n ~2 n' and m ~2 m'
  prove n + m ~2 n' + m'
}
descend add through Q2 using add_respects_parity

reject descend Phase4 through Q2 {
  counterexample 0 ~2 2 but r4(0) != r4(2)
}
```

### Parity, retention, and conditioning

For $P=\mathbb Z$ and $\Omega_2(n)=n\bmod2$,

$$
n\sim_2m
\iff
n-m\in2\mathbb Z,
\qquad
Q_2\cong\mathbb Z/2\mathbb Z.
$$

Addition passes descent. The operation $h(n)=\lfloor n/2\rfloor$ fails because $0\sim_2 2$ but $h(0)\not\sim_2h(2)$.

Now retain $r_4(n)=n\bmod4$. The combined witness is equivalent to the mod-4 witness:

$$
\sim_{2\oplus r_4}=\sim_4,
\qquad
Q_{2\oplus r_4}\cong\mathbb Z/4\mathbb Z
\twoheadrightarrow
Q_2.
$$

Conditioning on $r_4=0$ instead changes the source to $P_0=4\mathbb Z$; its parity witness has a single class. Because $0\sim_2 2$ while $r_4(0)\ne r_4(2)$, $r_4$ does not descend to $Q_2$. Therefore “form $Q_2$, then select residue $0\bmod4$” is undefined in this architecture. This is the typed form of the noncommuting-quotient warning.

## Application boundary: finite weighted ensembles

A retained seam or global holonomy can be modeled as `CTX` when it is a map on configurations. Fixing its value is `COND`; keeping it observable is `RET`. An exact gauge-fixing change of variables is a transport claim and needs a commuting certificate.

However, summing over link variables is a weighted pushforward or marginalization. It is not a `Set` quotient simply because information disappears. Claims about partition functions, normalized conditional ensembles, or probability laws remain external to the v0.3 core until a finite-weight or probabilistic profile supplies their semantics.

## Diagnostic catalogue

| Code | Rejection |
|---|---|
| `E101` | `QUO` has no declared `EQV`. |
| `E204` | An induced quotient operation or transport has no valid `DSC` certificate. |
| `E301` | `CPL` omits the structure and universal property being added. |
| `E407` | A refinement arrow points coarse → fine. |
| `E512` | The requested quotient–image comparison is unsupported by the active profile. |
| `E610` | A statement crosses equality lanes without a constructor or proof. |
| `E611` | `CTX` lacks a typed map or semantic role. |
| `E612` | `COND` lacks a declared context fiber. |
| `E613` | Post-quotient conditioning is requested without context descent. |
| `E614` | A changed architecture is reused without a declared map. |
| `E615` | Weighted marginalization is requested in the `Set` profile. |
| `E701` | An execution digest is asserted to prove witness equivalence or correctness. |
| `E702` | Distinct diagnostics are asserted to be independent without an independence certificate. |

## Illustrative typed machine record

```json
{
  "schema": "gqg-set-0.3",
  "profile": "Set",
  "source": {"id": "P", "presentation": "Integers"},
  "witness": {
    "id": "Parity",
    "observation": {
      "id": "omega2",
      "domain": "P",
      "codomain": "Z/2Z",
      "definition": "n mod 2"
    }
  },
  "equivalence": "kernel_pair(omega2)",
  "quotient": {"id": "Q2", "map": "q2"},
  "context": {
    "id": "Phase4",
    "map": {
      "id": "r4",
      "domain": "P",
      "codomain": "Z/4Z",
      "definition": "n mod 4"
    }
  },
  "retention": {
    "observation": "pair(omega2,r4)",
    "quotient": "Q2_with_Phase4",
    "comparison": "Q2_with_Phase4 ->> Q2"
  },
  "condition": {"context": "Phase4", "value": "0", "source": "P0"},
  "descent_checks": [
    {
      "map": "r4",
      "through": "Q2",
      "status": "rejected",
      "counterexample": "0 ~2 2 but r4(0) != r4(2)"
    }
  ],
  "realizations": []
}
```

This record is illustrative. A production schema must replace free-form expressions with expression AST nodes, define stable identifiers, and specify a canonicalization algorithm. Only then should canonical identity be a digest of canonical JSON for the AST. Prime products may remain unordered feature signatures useful for indexing token occurrence, but they are not syntax because they lose order, direction, scope, and binding.

## v0.3 acceptance target

- **Parseability:** one valid sentence produces one unambiguous AST.
- **Soundness:** accepted trees satisfy the declared formation rules.
- **Retention correctness:** `RET` constructs the joint observation and emits fine → coarse comparison only.
- **Conditioning correctness:** `COND` constructs a source fiber and never masquerades as source equality or weighted conditional probability.
- **Descent correctness:** the checker constructs $\bar T$ or $\bar r$ only from a valid certificate and rejects the mod-4 context on the parity quotient.
- **Realization separation:** semantic witness identity and execution provenance occupy different typed records.
- **Rendering stability:** text and diagrams emitted from one accepted AST preserve the same semantic structure.
- **Diagnostic value:** rejected trees receive local, actionable errors.
- **Accessible rendering:** meaning survives without color or decorative glyphs.

**Implementation milestone:** parse the `Set` profile; validate parity, retained mod-4 context, conditioned fibers, failed context descent, and ordinary operation descent; emit canonical JSON; and render labelled and accessibility-first views from the same AST.

## Frozen compact laws

$$
\boxed{
\textbf{No observational quotient without a declared witness; no conditioned claim without a declared context fiber; no transport across a changed architecture without descent.}
}
$$

$$
\boxed{
\textbf{What the witness forgets determines its equivalence; what it retains determines its refinement or condition. Neither may change silently.}
}
$$

**No crown. No proof by resemblance. No silent witness change.**

---

**License:** CC0 1.0 Universal. To the extent possible under law, the author has waived all copyright and related or neighboring rights to this work. No attribution required. <https://creativecommons.org/publicdomain/zero/1.0/>
