---
title: "Geometric Quotient Grammar"
subtitle: "A Witness-Relative Framework for Identification, Descent, and Completion"
author: "Pattern Monkey"
date: "August 10, 2026"
version: "0.1"
status: "Working preprint - conceptual and formal synthesis"
license: "CC0 1.0 Universal - Public Domain"
---

<!-- PDF_BODY_START -->

# Abstract

Many routine mathematical identifications are induced not by equality of presented objects but by the inability of a fixed observation system to distinguish them. This paper proposes **Geometric Quotient Grammar** (GQG) as a typed framework for making that passage explicit. A GQG begins with presented source objects and a declared family of witness-indexed observation maps. Their common fibers induce an observational equivalence; quotienting identifies exactly those objects that the declared system cannot separate. A given source operation descends exactly when this equivalence is a congruence for that operation, and any subsequent completion must be specified independently.

The multiplication representation of bounded measurable functions on $L^2(X,\mu)$ provides the canonical example. For an arbitrary measure space, the representation kernel consists of functions vanishing locally almost everywhere. The induced faithful representation factors through $L^\infty(\mu_{\mathrm{sf}})$; its norm is induced by the locally essential supremum seminorm on source functions. The example also separates two logically distinct thresholds: semifinite reduction repairs a failure of visibility, while localizability of the reduced measure is the condition for the familiar duality and von Neumann-algebraic conclusions. If localizability fails, passage to a separately specified localizable realization is an additional construction.

The component mechanisms - kernel pairs, equivalence relations, quotients, congruences, observational equivalence, and completion - are classical. The proposed contribution is a cross-domain typed synthesis: presentation, declared observation, separation, quotient, descent, and separately typed completion. GQG distinguishes source equality, witness-relative equivalence, quotient equality, and statements of equality or convergence after a specified completion; records witness refinement through canonical quotient maps; and treats the arrangement of induced partitions as an order-theoretic discrimination geometry.

**Keywords:** quotient, observational equivalence, witness system, kernel pair, congruence, identifiability, completion, multiplication representation, localizable measure space.

\newpage

# 1. Introduction

Mathematics routinely suppresses the construction by which an apparent identity becomes legitimate. A bounded measurable function is written as its multiplication operator. A group element is treated through an action or representation. Two pseudometric points are treated as one when their distance is zero. Two automaton histories are merged when no admissible continuation separates their future behavior. A parameter is called unidentified when every admissible experiment produces the same distribution under multiple source values.

These cases share a pattern, but the pattern has several types that ordinary notation can blur:

1. equality of source objects;
2. indistinguishability under a declared observation system;
3. equality of equivalence classes in a quotient;
4. equality or convergence after some later completion.

The central thesis of this paper is that those judgments should remain visibly distinct. Given presented objects $\mathcal P$ and a fixed family of observations $\mathcal W$, the identity licensed by that observational context is equality in the fibers of the aggregate observation map, not necessarily equality in $\mathcal P$. Passing to $\mathcal P/{\sim_{\mathcal W}}$ records the collapse. Source operations descend only after representative-independence is established. Completion answers a further structural question and requires its own type, hypotheses, and universal property.

We call this sequence **Geometric Quotient Grammar**. "Grammar" names the order and typing of its permitted constructions. "Geometric" names the refinement structure of the observational fibers: witness systems generate partitions of the source, stronger systems refine those partitions, and the resulting quotient maps reverse that refinement. No metric, manifold, topology, or algebraic-geometric quotient is assumed unless supplied by an example.

The canonical example is the multiplication representation

$$
\pi:B(X,\Sigma)\longrightarrow B(L^2(X,\mu)),
\qquad
\pi(f)=M_f.
$$

For arbitrary measures, its kernel is not generally the set of ordinarily almost-everywhere-zero functions. It is the set of functions vanishing locally almost everywhere. Consequently, the represented algebra is naturally $L^\infty(\mu_{\mathrm{sf}})$, where $\mu_{\mathrm{sf}}$ is the semifinite reduction. This example makes the full sequence visible: actual source functions, finite-measure witnesses, observational collapse, quotient factorization, descended algebraic operations, and a second completeness threshold controlled by localizability.

## 1.1 Contribution and nonclaim

GQG does **not** introduce a new notion of quotient equivalence. Testing semantics, universal algebra, category theory, automata, coalgebra, statistics, Chu spaces, abstract interpretation, and recent bounded-observer models already contain close relatives. The proposed contribution is architectural:

- a single typed signature for declaring source objects and admissible witnesses;
- a visible distinction among source equality, observational equivalence, quotient equality, and statements made after a specified completion;
- an order-theoretic discrimination geometry for witness refinement;
- explicit descent tests for operations and transformations;
- an insistence that the completion notion be named rather than smuggled into quotient language.

The Hidden Quotient is the paper's worked measure-theoretic and operator-algebraic instance.
For editorial audit, the paper also carries a claim-status ledger separating classical theorem, new definition, derived proposition, declared interpretation, and open problem.

The original contribution claimed here is therefore narrow: **a proposed comparative normal form and status-audited vocabulary for quotient constructions with witness systems as explicit data**. Whether that synthesis develops into a broader mathematical theory depends on the comparison, morphism, closure, noisy-witness, and completion results proposed in Section 10.

## 1.2 Claim-status notation

The manuscript uses the following labels.

| Tag | Status | Meaning |
|---|---|---|
| **[CT]** | Classical theorem | Established mathematics, proved or cited under stated hypotheses |
| **[ND]** | Manuscript definition | Terminology or structure introduced in this manuscript; not a claim of historical priority |
| **[DP]** | Derived proposition | Immediate or elementary consequence of the definitions |
| **[DI]** | Declared interpretation | Expository language, not mathematical entailment |
| **[OP]** | Open problem | Proposed research direction or unestablished extension |

This ledger is part of the method. A slogan may teach a theorem without becoming one.

# 2. Mathematical preliminaries

## 2.1 Quotients and kernel pairs

Let $F:P\to Y$ be a map of sets. Its **kernel pair** is

$$
\operatorname{Eq}(F)
=
\{(x,y)\in P\times P:F(x)=F(y)\}.
$$

It is an equivalence relation. The quotient map

$$
q:P\twoheadrightarrow P/{\operatorname{Eq}(F)}
$$

is generally noninjective. The map that becomes injective is the induced map

$$
\overline F:P/{\operatorname{Eq}(F)}\longrightarrow Y,
\qquad
\overline F([x])=F(x),
$$

whose image is $\operatorname{im}F$. Thus

$$
P/{\operatorname{Eq}(F)}\cong\operatorname{im}F
$$

as sets. This is the coimage-image factorization familiar from elementary set theory and categorical quotient theory (Barr, 1971; Mac Lane, 1998).

The word **kernel** requires more structure. If $F$ is a linear map, then

$$
F(x)=F(y)
\iff
x-y\in\ker F.
$$

For group homomorphisms the relation is controlled by a normal subgroup; for universal algebras it is a kernel congruence. For arbitrary observation maps, the safe general object is the kernel pair.

## 2.2 Congruence and descent

Let $P$ carry an $n$-ary operation $c:P^n\to P$. An equivalence relation $\sim$ is a **congruence** for $c$ when

$$
x_i\sim y_i\quad(1\le i\le n)
\quad\Longrightarrow\quad
c(x_1,\ldots,x_n)\sim c(y_1,\ldots,y_n).
$$

Exactly under this condition, the formula

$$
\overline c([x_1],\ldots,[x_n])
=
[c(x_1,\ldots,x_n)]
$$

is independent of representatives. This is the classical descent criterion of universal algebra (Birkhoff, 1935).

## 2.3 Completion has a type

"Completion" has no unqualified mathematical meaning. Metric completion, Banach completion, Dedekind-MacNeille completion, weak-operator closure, exact completion, and strictly localizable realization solve different problems (Carboni and Vitale, 1998, for exact completion). Some completion constructions themselves use quotients; therefore quotient and completion are not universally disjoint mechanisms. The valid design rule is narrower:

> When a construction first removes witness-invisible distinctions and later adjoins limits, suprema, densities, or effective quotients, the two purposes must be separately typed.

For example, a pseudometric space is commonly separated by quotienting zero-distance points and then completed metrically. In the Hidden Quotient, the $C^*$-quotient is already norm-complete; localizability concerns order completeness and represented weak closure, not a second norm completion.

# 3. Geometric Quotient Grammar

## 3.1 Witness presentations and full specifications

**Definition 3.1 [ND] - Witness presentation and GQG specification.** A set-level witness presentation is

$$
\mathsf G
=
\left(
\mathcal P,
\mathcal W,
\{(\mathcal O_w,\omega_w)\}_{w\in\mathcal W}
\right),
$$

where:

- $\mathcal P$ is a set of presented source objects;
- $\mathcal W$ is a declared witness family;
- $\mathcal O_w$ is the outcome set for witness $w$;
- $\omega_w:\mathcal P\to\mathcal O_w$ is its observation map.

The aggregate observation is

$$
\Omega_{\mathsf G}:\mathcal P
\longrightarrow
\prod_{w\in\mathcal W}\mathcal O_w,
\qquad
\Omega_{\mathsf G}(x)
=
(\omega_w(x))_{w\in\mathcal W}.
$$

The induced observational equivalence is derived data:

$$
x\sim_{\mathsf G}y
\iff
\Omega_{\mathsf G}(x)=\Omega_{\mathsf G}(y).
$$

Write

$$
Q_{\mathsf G}=\mathcal P/{\sim_{\mathsf G}},
\qquad
q_{\mathsf G}(x)=[x]_{\mathsf G}.
$$

Deriving $\sim_{\mathsf G}$ and $Q_{\mathsf G}$ from the observation maps prevents a separately declared equivalence from disagreeing with the witnesses that supposedly justify it.

A full GQG specification is

$$
\mathbf G
=
(\mathsf G,\mathcal C,\mathfrak K?),
$$

where $\mathsf G$ is a witness presentation, $\mathcal C$ is a possibly empty family of source operations or transformations selected for descent, and $\mathfrak K?$ is an optional, separately typed completion specification for the surviving quotient structure. The witness layer $\mathsf G$ determines the equivalence and quotient; membership in $\mathcal C$ does not guarantee descent, and the optional completion does not follow from the kernel pair. GQG is the framework that keeps these stages typed and records the proof obligations between them.

## 3.2 Kernel-pair factorization

**Proposition 3.2 [DP] - Observational factorization.** The relation $\sim_{\mathsf G}$ is the kernel pair of $\Omega_{\mathsf G}$. There is a unique injective map

$$
\overline\Omega_{\mathsf G}:Q_{\mathsf G}
\longrightarrow
\prod_{w\in\mathcal W}\mathcal O_w
$$

such that

$$
\Omega_{\mathsf G}
=
\overline\Omega_{\mathsf G}\circ q_{\mathsf G}.
$$

Its image is $\operatorname{im}\Omega_{\mathsf G}$, so

$$
Q_{\mathsf G}\cong\operatorname{im}\Omega_{\mathsf G}.
$$

**Proof.** Equality in every outcome set is reflexive, symmetric, and transitive. Define $\overline\Omega_{\mathsf G}([x])=\Omega_{\mathsf G}(x)$. It is well-defined because equivalent representatives have identical aggregate observations. If two classes have the same image, their representatives are equivalent, so the classes coincide. $\square$

The architecture is therefore

$$
\boxed{
\mathcal P
\twoheadrightarrow
Q_{\mathsf G}
\xrightarrow{\ \cong\ }
\operatorname{im}\Omega_{\mathsf G}
\hookrightarrow
\prod_w\mathcal O_w.
}
$$

The quotient map is not "faithful." It is the induced observation $\overline\Omega_{\mathsf G}$ that is injective on quotient classes.

## 3.3 Typed identity

There are three different judgments:

$$
x=_{\mathcal P}y,
\qquad
x\sim_{\mathsf G}y,
\qquad
q_{\mathsf G}(x)=_{Q_{\mathsf G}}q_{\mathsf G}(y).
$$

**Proposition 3.3 [DP] - Typed identity law.** For all $x,y\in\mathcal P$, the following two statements hold:

$$
\begin{aligned}
x=_{\mathcal P}y
&\Longrightarrow
x\sim_{\mathsf G}y,\\
x\sim_{\mathsf G}y
&\Longleftrightarrow
q_{\mathsf G}(x)=_{Q_{\mathsf G}}q_{\mathsf G}(y).
\end{aligned}
$$

The converse $x\sim_{\mathsf G}y\Rightarrow x=y$ holds exactly when $\Omega_{\mathsf G}$ is injective.

Thus quotienting does not rewrite source equality. It creates a new type in which multiple source objects may have equal images. Even $[x]_{\mathsf G}$ and $\Omega_{\mathsf G}(x)$ are not literally the same typed object; they correspond through the canonical bijection with the observation image.

## 3.4 Universal property

**Proposition 3.4 [CT] - Quotient factorization.** If $F:\mathcal P\to Y$ satisfies

$$
x\sim_{\mathsf G}y\Longrightarrow F(x)=F(y),
$$

then there exists a unique $\overline F:Q_{\mathsf G}\to Y$ with

$$
F=\overline F\circ q_{\mathsf G}.
$$

This is the precise content of the phrase "depends only on what survives the witnesses."

## 3.5 The first law

The formal design law of GQG is:

$$
\boxed{
\text{No quotient identification without a declared observation system.}
}
$$

This is a methodological rule of GQG, not a theorem that all quotients in mathematics must be presented by witnesses. Mathematics may begin directly with an equivalence relation. GQG is designed for settings where the identification is claimed to be observationally earned.

# 4. Discrimination geometry and the elementary calculus

## 4.1 Refinement order

Let $\mathsf G$ and $\mathsf H$ be witness presentations on the same source $\mathcal P$.

**Definition 4.1 [ND] - Discrimination preorder.** Say that $\mathsf H$ is at least as discriminating as $\mathsf G$, written

$$
\mathsf H\succeq\mathsf G,
$$

when

$$
\operatorname{Eq}(\Omega_{\mathsf H})
\subseteq
\operatorname{Eq}(\Omega_{\mathsf G}).
$$

The more discriminating system has smaller observational fibers and a finer partition of the source.

**Proposition 4.2 [DP] - Refinement map.** If $\mathsf H\succeq\mathsf G$, then there is a canonical surjection

$$
\rho_{\mathsf H,\mathsf G}:Q_{\mathsf H}
\twoheadrightarrow Q_{\mathsf G},
\qquad
[x]_{\mathsf H}\longmapsto[x]_{\mathsf G},
$$

and

$$
q_{\mathsf G}
=
\rho_{\mathsf H,\mathsf G}\circ q_{\mathsf H}.
$$

**Proof.** If $x\sim_{\mathsf H}y$, relation inclusion gives $x\sim_{\mathsf G}y$, so the formula is well-defined. Every coarse class has a source representative, proving surjectivity. $\square$

If $\mathcal W\subseteq\mathcal W'$ and all old observations remain unchanged, then the larger witness system is at least as discriminating. Adding witnesses may split existing classes; it cannot merge them. Replacing a witness family can instead produce incomparable partitions.

For example, on $\mathcal P=\{0,1,2\}$, the partitions

$$
\{0,2\}\mid\{1\}
\qquad\text{and}\qquad
\{0\}\mid\{1,2\}
$$

are incomparable.

## 4.2 Discernibility equivalence

**Definition 4.3 [ND].** Two witness presentations are **discernibility-equivalent** when they induce the same kernel pair.

**Proposition 4.4 [DP].** The following are equivalent:

1. $\operatorname{Eq}(\Omega_{\mathsf G})=\operatorname{Eq}(\Omega_{\mathsf H})$;
2. each presentation refines the other;
3. there is a unique bijection
   $$
   \beta:\operatorname{im}\Omega_{\mathsf G}
   \longrightarrow
   \operatorname{im}\Omega_{\mathsf H}
   $$
   with $\beta\circ\Omega_{\mathsf G}=\Omega_{\mathsf H}$.

Discernibility equivalence is weaker than representation equivalence. The maps $x\mapsto x$ and $x\mapsto2x$ on $\mathbb R$ have the same kernel pair but different scales. A kernel pair records which pairs the witnesses distinguish; it carries no magnitude of distinction without additional structure. Norm preservation requires additional structure and an isometry theorem.

## 4.3 Joins of witness families

Given $\mathsf G$ and $\mathsf H$ on the same source, form the combined presentation $\mathsf G\oplus\mathsf H$ using the tagged disjoint union

$$
\mathcal W_{\mathsf G}\sqcup\mathcal W_{\mathsf H}
$$

of their witness indices. Then

$$
\operatorname{Eq}(\Omega_{\mathsf G\oplus\mathsf H})
=
\operatorname{Eq}(\Omega_{\mathsf G})
\cap
\operatorname{Eq}(\Omega_{\mathsf H}).
$$

Thus combining witnesses takes the common refinement of their source partitions. With equivalence relations ordered by reverse inclusion, the assignment

$$
[\mathsf G]\longmapsto\operatorname{Eq}(\Omega_{\mathsf G})
$$

is an order embedding from discernibility classes, and $\mathsf G\oplus\mathsf H$ is a join in that discrimination order. Under ordinary inclusion of equivalence relations, the same construction is an intersection and hence a meet. This order-theoretic structure is the minimal technical content of the word "geometric" in GQG.

The geometry is not a metric geometry. It is the arrangement of observational fibers under refinement, combination, and quotient reversal.

## 4.4 Descent of operations

Suppose $\mathcal P$ carries source operations $c:\mathcal P^n\to\mathcal P$.

**Proposition 4.5 [CT] - Descent criterion.** The formula

$$
\overline c([x_1],\ldots,[x_n])
=
[c(x_1,\ldots,x_n)]
$$

defines an operation on $Q_{\mathsf G}$ if and only if $\sim_{\mathsf G}$ is a congruence for $c$.

Arbitrary observation maps do not guarantee descent. Let $\mathcal P=(\mathbb Z,+)$ and define

$$
\omega(n)=
\begin{cases}
0,&n=0,\\
1,&n\ne0.
\end{cases}
$$

Then $1\sim2$, but

$$
1+(-1)=0
\not\sim
1=2+(-1).
$$

Addition does not descend through this quotient.

The grammatical sequence is therefore

$$
\boxed{
\text{Present}
\to
\text{Declare witnesses}
\to
\text{Observe}
\to
\text{Quotient}
\to
\text{Prove descent}
\to
\text{Compose}.
}
$$

## 4.5 Separately typed completion

**Definition 4.6 [ND] - Completion specification.** For a structured quotient $Q$, a completion specification is

$$
\mathfrak K
=
(\mathcal A,\mathcal A_{\mathrm{cmp}},\widehat Q,\eta,\mathsf U),
$$

where $\mathcal A$ is the declared ambient category of structured objects, $\mathcal A_{\mathrm{cmp}}$ is its declared class or full subcategory of complete objects, $\widehat Q\in\mathcal A_{\mathrm{cmp}}$, $\eta:Q\to\widehat Q$ is a structure-preserving morphism, and $\mathsf U$ is a stated density or universal property characterizing the construction. Injectivity of $\eta$ is not assumed unless the chosen completion notion requires it.

The observation kernel pair alone cannot determine a completion. The vector space $c_{00}$ with identity observations has no quotient collapse, yet its completion is $\ell^1$ under the $\ell^1$ norm and $\ell^2$ under the $\ell^2$ norm. Completion therefore appears in the grammar only after its ambient structure and completion notion are named.

# 5. Canonical instance: the Hidden Quotient

## 5.1 Pointwise bounded measurable functions prior to quotienting

Let $(X,\Sigma,\mu)$ be an arbitrary measure space, with no semifiniteness or sigma-finiteness assumption. Begin with actual bounded measurable functions

$$
B(X,\Sigma)
=
\{f:X\to\mathbb C:f\text{ measurable and bounded}\},
$$

equipped with pointwise operations and the ordinary supremum norm. Define

$$
\pi:B(X,\Sigma)\longrightarrow B(L^2(X,\mu)),
\qquad
\pi(f)=M_f,
$$

where

$$
(M_fg)(x)=f(x)g(x).
$$

The map $\pi$ is a $*$-homomorphism and is contractive. It is unit-preserving; in the edge case $L^2(\mu)=\{0\}$, we use the convention that $B(\{0\})=\{0\}$ is unital with identity $0$. Its kernel is therefore a closed self-adjoint two-sided ideal.

## 5.2 Three discernibility-equivalent witness systems

Let

$$
\Sigma_{\mathrm{fin}}
=
\{E\in\Sigma:\mu(E)<\infty\}.
$$

The same observational equivalence may be generated in three ways.

**Finite-window witnesses:**

$$
\omega_E(f)=f\chi_E\in L^2(\mu),
\qquad E\in\Sigma_{\mathrm{fin}}.
$$

**All-vector witnesses:**

$$
\theta_g(f)=fg\in L^2(\mu),
\qquad g\in L^2(\mu).
$$

**Operator observation:**

$$
\pi(f)=M_f\in B(L^2(\mu)).
$$

The first family has a special internality property: each indicator $\chi_E$ is itself a vector in the represented Hilbert space. The witnesses are not external inspectors added after the fact.

Write $\mathsf G_{\mathrm{fin}}$, $\mathsf G_{\mathrm{vec}}$, and $\mathsf G_\pi$ for these three presentations on the common source $B(X,\Sigma)$. Theorem 5.1 shows that they are discernibility-equivalent. We write their common relation as

$$
f\sim_{\mathrm{loc}}h.
$$

## 5.3 The hidden kernel

**Theorem 5.1 [CT] - Local almost-everywhere kernel.** For $f,h\in B(X,\Sigma)$, the following are equivalent:

1. $M_f=M_h$;
2. $fg=hg$ for every $g\in L^2(\mu)$;
3. $f\chi_E=h\chi_E$ in $L^2(\mu)$ for every $E\in\Sigma_{\mathrm{fin}}$;
4. $f=h$ locally almost everywhere, meaning almost everywhere on every finite-measure set.

**Proof.** Operator equality is equality on every vector, and testing against $\chi_E$ gives finite-window equality. For each $E\in\Sigma_{\mathrm{fin}}$,

$$
f\chi_E=h\chi_E\text{ in }L^2
\iff
f=h\text{ almost everywhere on }E,
$$

which proves $(3)\Longleftrightarrow(4)$. Conversely, put $a=f-h$ and let $g\in L^2$. Then

$$
\{|g|>0\}
=
\bigcup_{n\ge1}\{|g|\ge1/n\}.
$$

Chebyshev's inequality gives

$$
\mu\{|g|\ge1/n\}
\le
n^2\|g\|_2^2
<\infty.
$$

Finite-window equality makes $a=0$ almost everywhere on each set in the union, hence $ag=0$ almost everywhere. Therefore $M_f=M_h$. $\square$

Consequently,

$$
\ker\pi
=
K_{\mathrm{loc}}
=
\{f:f=0\text{ locally almost everywhere}\}.
$$

## 5.4 The infinite-measure-point counterexample

Let

$$
X=[0,1]\sqcup\{p\},
$$

with Lebesgue measure on $[0,1]$ and

$$
\mu(\{p\})=\infty.
$$

Every finite-measure set is contained in $[0,1]$. Every square-integrable measurable representative satisfies $g(p)=0$. Thus

$$
L^2(X,\mu)\cong L^2[0,1].
$$

For

$$
f=\chi_{\{p\}},
$$

one has

$$
f\ne0\quad\text{in }B(X,\Sigma),
$$

but

$$
f\sim_{\mathrm{loc}}0,
\qquad
[f]_{Q_\mu}=[0]_{Q_\mu},
\qquad
M_f=0.
$$

Moreover,

$$
\operatorname*{ess\,sup}_{\mu}|f|=1,
\qquad
\|M_f\|=0.
$$

This example separates source distinction, observational equivalence, quotient equality, ordinary essential magnitude, and represented magnitude in one line.

It does **not** prove that the point $p$ is nonexistent. It proves that the fixed $L^2$ multiplication representation does not record its distinction.

## 5.5 Quotient, induced faithfulness, and norm

Since $K_{\mathrm{loc}}$ is a closed self-adjoint ideal,

$$
Q_\mu
=
B(X,\Sigma)/K_{\mathrm{loc}}
$$

is a $C^*$-algebra. Define the locally essential supremum **seminorm on the source** by

$$
p_{\mathrm{loc}}(f)
=
\inf\{c\ge0:\{|f|>c\}\text{ is locally null}\}.
$$

Its zero set is $K_{\mathrm{loc}}$, so it induces a norm on $Q_\mu$.

**Proposition 5.2 [CT] - Quotient norm and represented norm.** For every $f\in B(X,\Sigma)$,

$$
\|[f]\|_{Q_\mu}
=
p_{\mathrm{loc}}(f)
=
\|M_f\|.
$$

**Proof.** The quotient norm is

$$
\|[f]\|_{Q_\mu}
=
\inf_{k\in K_{\mathrm{loc}}}\|f+k\|_\infty.
$$

If $A_c=\{|f|>c\}$ is locally null, then

$$
k=-f\chi_{A_c}\in K_{\mathrm{loc}},
\qquad
\|f+k\|_\infty\le c.
$$

Conversely, if $k\in K_{\mathrm{loc}}$ and $\|f+k\|_\infty\le c$, then

$$
\{|f|>c\}\subseteq\{k\ne0\},
$$

which is locally null. Taking infima proves $\|[f]\|_{Q_\mu}=p_{\mathrm{loc}}(f)$. The induced representation

$$
\overline\pi:Q_\mu\longrightarrow B(L^2(\mu)),
\qquad
\overline\pi([f])=M_f,
$$

is injective. An injective $*$-homomorphism between $C^*$-algebras is isometric, giving the second equality. $\square$

The logical order is

$$
\text{quotient factorization}
\Longrightarrow
\text{injective induced representation}
\Longrightarrow
\text{isometry by }C^*\text{-theory}.
$$

The quotient map is always contractive. It is injective - and therefore isometric - exactly when $K_{\mathrm{loc}}=\{0\}$; when the kernel is nonzero, it intentionally collapses it.

The operator norm is universally defined by the closed unit ball:

$$
\|M_f\|
=
\sup_{\|g\|_2\le1}\|fg\|_2.
$$

The unit-sphere formula is equivalent when $L^2\ne\{0\}$, but its indexing set is empty on the zero Hilbert space. The unit-ball formula covers the infinite-atom edge case without exception.

## 5.6 Semifinite reduction

Define

$$
\mu_{\mathrm{sf}}(E)
=
\sup\{\mu(F):F\subseteq E,\ F\in\Sigma,\ \mu(F)<\infty\}.
$$

**Proposition 5.3 [CT] - Semifinite reduction.** The set function $\mu_{\mathrm{sf}}$ is a semifinite measure, $\mu_{\mathrm{sf}}\le\mu$, and it agrees with $\mu$ on every set of finite $\mu$-measure. Moreover,

$$
\mathcal N_{\mu_{\mathrm{sf}}}
=
\mathcal N_{\mathrm{loc}}.
$$

Consequently,

$$
B(X,\Sigma)/K_{\mathrm{loc}}
\cong
L^\infty(\mu_{\mathrm{sf}})
$$

isometrically as $C^*$-algebras. For $1\le p<\infty$ there are canonical isometric identifications

$$
L^p(\mu)\cong L^p(\mu_{\mathrm{sf}}).
$$

These measure-theoretic facts are the standard semifinite-reduction theorem (Fremlin, 2001, Sections 211 and 213). If $\mu$ is semifinite, local nullity equals ordinary nullity and the quotient reduces to the familiar $L^\infty(\mu)$.

## 5.7 Localizability and the second threshold

The quotient is already norm-complete. A separate question is whether the reduced measure algebra

$$
\Sigma/\mathcal N_{\mathrm{loc}}
$$

is Dedekind complete. Here "localizable" follows Fremlin's convention: a measure is semifinite and its measure algebra is Dedekind complete. Since $\mu_{\mathrm{sf}}$ is already semifinite, its localizability is exactly the displayed order-completeness condition.

**Theorem 5.4 [CT] - Localizability equivalences.** For every measure space $(X,\Sigma,\mu)$, the canonical map

$$
Q_\mu\longrightarrow (L^1(\mu))^*,
\qquad
[f]\longmapsto\left(g\mapsto\int fg\,d\mu\right)
$$

is always isometric. The following are equivalent:

1. $\mu_{\mathrm{sf}}$ is localizable;
2. $\Sigma/\mathcal N_{\mathrm{loc}}$ is Dedekind complete;
3. the displayed canonical isometry $Q_\mu\to(L^1(\mu))^*$ is onto;
4. $\overline\pi(Q_\mu)$ is a von Neumann algebra on $L^2(\mu)$;
5. $\overline\pi(Q_\mu)$ is a maximal abelian $*$-subalgebra of $B(L^2(\mu))$.

These equivalences are external structural theorems, not consequences of the elementary kernel proof alone (Segal, 1951; Fremlin, 2001, Section 243G; De Pauw, 2024; Blecher, Goldstein, and Labuschagne, 2022, Theorem 5.2). When they fail, passing to a separately specified localizable or strictly localizable realization is an additional construction; it is not an automatic consequence of the visibility quotient (Bouafia and De Pauw, 2023).

# 6. Two thresholds, separately typed

The Hidden Quotient exposes two failures.

| Threshold | Question | Failure | Criterion or construction | What it does not do |
|---|---|---|---|---|
| Visibility | Which source distinctions can the fixed witnesses detect? | Positive mass may have no finite positive-measure handle | Quotient by local nullity; semifinite reduction | Does not create missing suprema |
| Gluing / order completeness | Can surviving compatible pieces assemble into required global objects? | The reduced Boolean algebra may lack suprema | Localizability is the criterion; a specified localizable realization is an optional further construction | Is not another name for deleting invisible mass |

Passing from $\mu$ to $\mu_{\mathrm{sf}}$ leaves the Boolean algebra $\Sigma/\mathcal N_{\mathrm{loc}}$ unchanged. It repairs the visibility seam but cannot by itself repair Dedekind incompleteness. When Dedekind completeness fails, a localizable or strictly localizable realization may be constructed separately under its own specification.

The paper therefore uses the following rule:

$$
\boxed{
\text{First ask what the declared witnesses can see.}
\quad
\text{Then ask whether the surviving pieces glue.}
}
$$

This is exact for the Hidden Quotient. It is not asserted as a universal temporal order for every categorical completion.

# 7. Additional classical instances

## 7.1 Myhill-Nerode

Let $L\subseteq\Sigma^*$ be a language. Take source objects $\mathcal P=\Sigma^*$ and witnesses $\mathcal W=\Sigma^*$, interpreted as possible continuations. Define

$$
\omega_z(x)
=
\mathbf 1_L(xz).
$$

Then

$$
x\sim_Ly
\iff
\mathbf 1_L(xz)=\mathbf 1_L(yz)
\quad\text{for every continuation }z.
$$

No admissible future continuation separates equivalent prefixes. The relation is a right congruence, and the quotient supplies the states of the minimal deterministic automaton when the quotient has finite index (Nerode, 1958). This is perhaps the cleanest classical instance of the full GQG pipeline.

## 7.2 Process tests and coalgebra

Testing semantics begins with processes and tests, then defines equivalence by the outcomes of those tests (De Nicola and Hennessy, 1984). Observation congruence adds the requirement that equivalence remain stable in appropriate contexts (Hennessy and Milner, 1985); compositional operational semantics supplies related congruence principles (Turi and Plotkin, 1997). In universal coalgebra, behavioral equivalence is equality under a common coalgebra morphism, or under final semantics when a final coalgebra exists. Its coincidence with relation-lifting bisimilarity, and with logical equivalence for a separating modal logic, requires additional hypotheses (Rutten, 2000; Schröder, 2008).

These are direct antecedents, not applications discovered by GQG. GQG proposes a common status and typing vocabulary in which their observation maps, quotient relations, and congruence requirements can be compared with other domains.

## 7.3 Chu spaces

A Chu space is a two-sorted evaluation structure

$$
r:X\times A\to K
$$

of points against attributes or tests. Repeated rows represent points with identical test profiles. Quotienting repeated rows gives the separated collapse; the biextensional collapse removes both repeated rows and repeated columns (Pratt, 2003). This is a particularly close abstract container for the pair $(\mathcal P,\mathcal W)$ and its evaluation map.

GQG differs mainly in emphasis: it foregrounds the source/quotient type distinction, witness refinement maps, descent of selected operations, and separately declared completion.

## 7.4 Statistical identifiability

For a statistical model $\theta\mapsto P_\theta$, define

$$
\theta\sim\theta'
\iff
P_\theta=P_{\theta'}.
$$

Identifiability is injectivity of this observation map. In a nonidentifiable model, the observationally estimable object is naturally a quotient or image rather than an individual source parameter (Rothenberg, 1971; McCullagh, 1999).

This example also marks a limit. Finite-sample power, approximate equality, experiment design, measurement error, and likelihood geometry are not captured by exact set-level GQG. They require probabilistic or metric witness structure. Calling a nonidentifiable direction a "kernel" is legitimate only when an actual linearized or homomorphic map supplies one.

## 7.5 Pseudometric separation and completion

For a pseudometric space $(P,d)$, take the profile observation

$$
\Omega(x)=d(x,\cdot).
$$

Then

$$
\Omega(x)=\Omega(y)
\iff
d(x,y)=0.
$$

The quotient by zero-distance points is a metric space. Its metric completion is a separate construction. This example shows why source separation and completion often appear consecutively while remaining different in purpose.

## 7.6 Bounded interaction

A 2026 arXiv preprint on finite POMDPs fixes a family of bounded controllers, identifies histories no controller in the family can distinguish, and studies the resulting canonical quotient and probe-family refinement (Nixon, 2026). It is direct prior art for bounded-witness quotienting. GQG therefore makes no novelty claim for observer-capacity-relative indistinguishability itself.

# 8. Relation to existing mathematics

| Established framework | Shared mechanism | GQG emphasis |
|---|---|---|
| Universal algebra | Kernel congruence and quotient operations | Witness system is explicit and audited before descent |
| Category theory | Kernel pairs, coequalizers, image factorization | Typed source, observation, quotient, and comparison layers |
| Testing semantics | Tests induce observational equivalence | Cross-domain witness refinement and completion ledger |
| Myhill-Nerode | Continuations separate histories; quotient minimizes | General witness syntax beyond languages |
| Universal coalgebra | Behavioral equivalence and separating logics | Common notation for observer-relative partitions |
| Chu spaces | Evaluation of points against attributes | Quotient descent and completion as first-class concerns |
| Statistical identifiability | Parameters identified through observable laws | Prohibition against algebraic kernel language without structure |
| Abstract interpretation | Declared information loss in an abstraction (Cousot and Cousot, 1977) | Exact fibers and quotient identity in version 0.1 |
| Completion theory | Adjoining limits, suprema, or effective quotients | Completion notion must be separately named |

Representative direct antecedents include testing semantics, kernel-pair quotients, Myhill-Nerode equivalence, Chu spaces, and Nixon's recent bounded-interaction construction.

Accordingly, GQG should presently be classified as a **conceptual and formal synthesis**. A stronger theory claim would require results not already inherited from those frameworks.

# 9. Scope and limitations

GQG is relative to a declared observation system. From

$$
x\sim_{\mathsf G}y
$$

one may conclude only that the observations in $\mathsf G$ assign the same outputs to $x$ and $y$. One may not conclude that $x=y$ in the source, that no enlarged system could separate them, or that the collapsed distinction is ontologically unreal.

The choice of witnesses is substantive. A family may be incomplete, purpose-specific, or incapable of recording distinctions important elsewhere. Enlarging the family may split quotient classes. Replacing it with a nonnested family may produce an incomparable quotient. GQG audits these changes; it does not independently select the correct domain witnesses.

The general construction does not always possess an algebraic kernel. Outside pointed, linear, or homomorphic settings, the proper object is a kernel pair. Source operations do not automatically survive quotienting. Each operation must satisfy the congruence condition, and partial operations require saturated domains.

Version 0.1 uses exact equality of observations. It does not yet model measurement error, statistical power, approximate equivalence, tolerance thresholds, adversarial missingness, or noisy witnesses. Those extensions require additional probability, metric, topology, or decision structure.

The Hidden Quotient is a canonical instance, not evidence that every domain has the same two thresholds or admits the same repairs. Its conclusions about localizability, $L^1$ duality, Radon-Nikodým representation, weak closure, and maximal abelianness depend on their exact measure-theoretic hypotheses.

The isometry in the Hidden Quotient is also special. A general injective observation need not preserve magnitude: $x\mapsto2x$ is injective but rescales distances. The equality

$$
\|M_f-M_h\|
=
\|[f]-[h]\|_{Q_\mu}
$$

comes from the $C^*$ theorem for injective $*$-homomorphisms, not from quotienting alone.

Finally, GQG entails no normative or empirical conclusions without an independently specified observation model and domain-specific validation.

# 10. Research program

The following questions determine whether GQG can move beyond synthesis.

## 10.1 Morphisms and categories [OP]

Define morphisms between witness presentations that may change source objects, witnesses, and outcome spaces while preserving observational evaluation. Determine when quotient formation is functorial and when change of witnesses admits adjoints.

## 10.2 Comparison of nonnested systems [OP]

Develop common refinements, common coarsenings, and obstruction criteria for witness systems whose induced partitions are incomparable. The lattice of equivalence relations gives an ambient answer in sets; structured categories may not preserve the required quotients.

## 10.3 Witness bases and saturation [OP]

Characterize minimal witness subfamilies that generate the same kernel pair. Given a fixed catalog of admissible observations, study closure under all observations constant on the induced quotient and the resulting Galois-style relation between witness families and equivalence relations.

## 10.4 Quotient-completion interaction [OP]

For a specified completion notion $\mathfrak K$, determine conditions under which completion commutes with an observational quotient, and construct counterexamples when it does not. Metric, order, weak-operator, and exact completions should be treated separately.

## 10.5 Approximate and probabilistic witnesses [OP]

Replace exact outcome equality with statistical, metric, or decision-theoretic comparison while retaining explicit error rates and power. Determine when approximate equivalence is transitive and when its quotient must be replaced by enriched, fuzzy, or probabilistic structure.

## 10.6 Computational questions [OP]

Study decidability and complexity of witness equivalence, minimal witness bases, quotient construction, and congruence closure. Myhill-Nerode supplies the classical finite-state benchmark.

## 10.7 Internal witnesses [OP]

The Hidden Quotient has internal witnesses: finite-measure indicators live inside the represented Hilbert space. Determine what additional structure follows when witnesses are objects or morphisms internal to the represented system rather than external tests.

# 11. Conclusion

Geometric Quotient Grammar makes explicit a construction that standard notation often hides. Presented objects are not identified merely because a convenient representation writes them the same way. A declared observation system first determines an equivalence relation; the quotient records that relation; operations descend only when representative-independence is proved; and completion, where required, is a separate construction with separate hypotheses.

The multiplication representation over an arbitrary measure space shows why the order matters. A function may be nonzero in the source while acting as the zero operator on the fixed $L^2$ representation. Quotienting by local almost-everywhere equality produces a quotient canonically isometric to $L^\infty(\mu_{\mathrm{sf}})$; its norm is induced by the locally essential supremum seminorm on source functions. Localizability then characterizes a second threshold - the existence of the required global suprema - that semifinite reduction does not settle.

The underlying mechanisms are classical. The proposed contribution of GQG is architectural: a common notation, an explicit claim-status discipline, an order-theoretic geometry of witness refinement, and a prohibition against silently moving among source equality, observational equivalence, quotient equality, and statements made only after a separately specified completion.

The first law is:

$$
\boxed{
\text{No quotient identification without a declared observation system.}
}
$$

Its human-language compression is:

$$
\boxed{
\textbf{Before asking whether two things are the same, ask what is allowed to tell them apart.}
}
$$

# Appendix A. Claim and provenance ledger

| Claim | Status | Provenance or condition |
|---|---|---|
| Witness presentation and full GQG specification | **[ND]** | Introduced here |
| Observational kernel-pair factorization | **[DP]** | Standard quotient theory, restated in GQG notation |
| Typed identity law | **[DP]** | Immediate from the quotient definition |
| Discrimination preorder and refinement map | **[DP]** | Relation inclusion on a common source |
| Combined witnesses induce relation intersection | **[DP]** | Direct calculation |
| Operation descent iff congruence | **[CT]** | Universal algebra |
| Completion specification is separately typed | **[ND]** | GQG design rule |
| Hidden kernel equals local-a.e.-zero functions | **[CT]** | Elementary proof in Section 5.3 |
| Quotient norm equals represented norm | **[CT]** | Quotient-norm calculation and injective $*$-homomorphism theorem |
| $Q_\mu\cong L^\infty(\mu_{\mathrm{sf}})$ | **[CT]** | Semifinite-reduction theorem |
| Localizability equivalences | **[CT]** | Segal, Fremlin, De Pauw, Blecher-Goldstein-Labuschagne |
| First law and teaching maxims | **[DI]** | Methodological compression, not an independent theorem |
| Academic novelty beyond synthesis | **[OP]** | Requires new comparison, morphism, or completion theorems |

# Appendix B. Technical provenance note

This edition incorporates mathematical corrections developed in the author's Hidden Quotient technical notes. In particular:

1. Indistinguishability is scoped to the fixed declared $L^2(X,\mu)$ representation.
2. Semifinite reduction and localizability address different defects.
3. Changing representation is a different test and may change commutants, multiplicity, weak closure, and maximal-abelian placement.
4. The induced representation, not the quotient map, is faithful and isometric.
5. Operator norm uses the closed unit ball when the zero Hilbert space is allowed.
6. Canonical isometric identifications $L^p(\mu)\cong L^p(\mu_{\mathrm{sf}})$ are not written as literal equality unless an identification convention is declared.

The mathematical results are logically independent of any companion interpretations.

# References

Barr, M. (1971). Exact categories. In *Exact Categories and Categories of Sheaves*, Lecture Notes in Mathematics 236, 1-120. Springer. <https://doi.org/10.1007/BFb0058580>

Birkhoff, G. (1935). On the structure of abstract algebras. *Proceedings of the Cambridge Philosophical Society*, 31(4), 433-454. <https://doi.org/10.1017/S0305004100013463>

Blecher, D. P., Goldstein, S., and Labuschagne, L. E. (2022). Abelian von Neumann algebras, measure algebras and $L^\infty$-spaces. *Expositiones Mathematicae*, 40(3), 758-818. <https://doi.org/10.1016/j.exmath.2021.11.005>

Bouafia, P., and De Pauw, T. (2023). Radon-Nikodýmification of arbitrary measure spaces. *Extracta Mathematicae*, 38(2), 139-203. <https://doi.org/10.17398/2605-5686.38.2.139>

Carboni, A., and Vitale, E. M. (1998). Regular and exact completions. *Journal of Pure and Applied Algebra*, 125, 79-116. <https://doi.org/10.1016/S0022-4049(96)00115-6>

Cousot, P., and Cousot, R. (1977). Abstract interpretation: A unified lattice model for static analysis of programs by construction or approximation of fixpoints. *POPL 1977*, 238-252. <https://doi.org/10.1145/512950.512973>

De Nicola, R., and Hennessy, M. C. B. (1984). Testing equivalences for processes. *Theoretical Computer Science*, 34, 83-133. <https://doi.org/10.1016/0304-3975(84)90113-0>

De Pauw, T. (2024). Undecidably semilocalizable metric measure spaces. *Communications in Contemporary Mathematics*, 26(4). <https://doi.org/10.1142/S0219199723500128>

Fremlin, D. H. (2001). *Measure Theory, Volume 2: Broad Foundations*. Colchester: Torres Fremlin. <https://www1.essex.ac.uk/maths/people/fremlin/mt.htm>

Hennessy, M., and Milner, R. (1985). Algebraic laws for nondeterminism and concurrency. *Journal of the ACM*, 32(1), 137-161. <https://doi.org/10.1145/2455.2460>

Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. <https://doi.org/10.1007/978-1-4757-4721-8>

McCullagh, P. (1999). Quotient spaces and statistical models. *Canadian Journal of Statistics*, 27(3), 447-456. <https://doi.org/10.2307/3316103>

Nerode, A. (1958). Linear automaton transformations. *Proceedings of the American Mathematical Society*, 9(4), 541-544. <https://doi.org/10.1090/S0002-9939-1958-0135681-9>

Nixon, A. T. (2026). The Myhill-Nerode theorem for bounded interaction: Canonical abstractions via agent-bounded indistinguishability. arXiv:2603.21399. Preprint. <https://arxiv.org/abs/2603.21399>

Pratt, V. R. (2003). Chu spaces as a semantic bridge between linear logic and mathematics. *Theoretical Computer Science*, 294(3), 439-471. <https://doi.org/10.1016/S0304-3975(01)00169-4>

Rothenberg, T. J. (1971). Identification in parametric models. *Econometrica*, 39(3), 577-591. <https://doi.org/10.2307/1913267>

Rutten, J. J. M. M. (2000). Universal coalgebra: A theory of systems. *Theoretical Computer Science*, 249(1), 3-80. <https://doi.org/10.1016/S0304-3975(00)00056-6>

Schröder, L. (2008). Expressivity of coalgebraic modal logic: The limits and beyond. *Theoretical Computer Science*, 390(2-3), 230-247. <https://doi.org/10.1016/j.tcs.2007.09.023>

Segal, I. E. (1951). Equivalences of measure spaces. *American Journal of Mathematics*, 73(2), 275-313. <https://doi.org/10.2307/2372178>

Turi, D., and Plotkin, G. D. (1997). Towards a mathematical operational semantics. *LICS 1997*, 280-291. <https://doi.org/10.1109/LICS.1997.614955>

# License and provenance

This working preprint is released under **CC0 1.0 Universal**. To the extent possible under law, the author has waived copyright and related rights.

The Hidden Quotient example originated in the author's longer technical and expository notes. The mathematical results in this paper are logically independent of the companion interpretations in those notes.
