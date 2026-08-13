---
title: "GQG Corecard"
subtitle: "Geometric Quotient Grammar v0.1"
author: "Pattern Monkey"
date: "August 10, 2026"
license: "CC0 1.0 Universal"
---

# Governing question

> **Before asking whether two things are the same, ask what is allowed to tell them apart.**

# Minimal presentation

A witness presentation is

$$
\mathsf G
=
\left(
\mathcal P,
\mathcal W,
\{(\mathcal O_w,\omega_w)\}_{w\in\mathcal W}
\right),
$$

with presented source objects $\mathcal P$, declared witnesses $\mathcal W$, outcome sets $\mathcal O_w$, and observation maps

$$
\omega_w:\mathcal P\to\mathcal O_w.
$$

The aggregate observation is

$$
\Omega_{\mathsf G}(x)
=
(\omega_w(x))_{w\in\mathcal W}.
$$

The observations induce

$$
x\sim_{\mathsf G}y
\iff
\Omega_{\mathsf G}(x)=\Omega_{\mathsf G}(y),
$$

and the quotient

$$
Q_{\mathsf G}=\mathcal P/{\sim_{\mathsf G}}.
$$

A full specification is $\mathbf G=(\mathsf G,\mathcal C,\mathfrak K?)$: witness layer, selected source operations for descent, and an optional completion specification.

# Typed identity

Keep three judgments separate:

$$
x=_{\mathcal P}y,
\qquad
x\sim_{\mathsf G}y,
\qquad
[x]_{\mathsf G}=_{Q_{\mathsf G}}[y]_{\mathsf G}.
$$

Always:

$$
x\sim_{\mathsf G}y
\iff
[x]_{\mathsf G}=[y]_{\mathsf G}.
$$

But in general:

$$
x\sim_{\mathsf G}y
\not\Rightarrow
x=y.
$$

# Factorization

The kernel-pair quotient gives

$$
\mathcal P
\twoheadrightarrow
Q_{\mathsf G}
\xrightarrow{\ \cong\ }
\operatorname{im}\Omega_{\mathsf G}
\hookrightarrow
\prod_w\mathcal O_w.
$$

The quotient map is generally noninjective. The induced observation on quotient classes is injective.

# Witness refinement

Say $\mathsf H$ is at least as discriminating as $\mathsf G$ when

$$
\operatorname{Eq}(\Omega_{\mathsf H})
\subseteq
\operatorname{Eq}(\Omega_{\mathsf G}).
$$

Then

$$
Q_{\mathsf H}\twoheadrightarrow Q_{\mathsf G}.
$$

More witnesses may split classes. Replacing a witness system may instead produce an incomparable partition.

# Descent before composition

An operation $c:\mathcal P^n\to\mathcal P$ descends precisely when

$$
x_i\sim_{\mathsf G}y_i\ \forall i
\Longrightarrow
c(x_1,\ldots,x_n)
\sim_{\mathsf G}
c(y_1,\ldots,y_n).
$$

Only then is

$$
\overline c([x_1],\ldots,[x_n])
=
[c(x_1,\ldots,x_n)]
$$

representative-independent.

# Completion is separate data

A completion specification must declare

$$
\mathfrak K=(\mathcal A,\mathcal A_{\mathrm{cmp}},\widehat Q,\eta,\mathsf U),
$$

including the ambient category, complete objects, structure-preserving map, and universal or density property. Metric, Banach, Dedekind, weak-operator, exact, and localizable completions are not interchangeable.

# Canonical Hidden Quotient instance

For an arbitrary measure space $(X,\Sigma,\mu)$,

$$
\mathcal P=B(X,\Sigma),
\qquad
\mathcal W=\{E\in\Sigma:\mu(E)<\infty\},
$$

$$
\omega_E(f)=f\chi_E\in L^2(\mu).
$$

Then

$$
f\sim g
\iff
f=g\text{ locally almost everywhere}
\iff
M_f=M_g.
$$

The induced representation

$$
\overline\pi:
B(X,\Sigma)/\ker\pi
\longrightarrow
B(L^2(\mu))
$$

is faithful and isometric, with

$$
p_{\mathrm{loc}}(f)
=
\inf\{c\ge0:\{|f|>c\}\text{ is locally null}\},
$$

$$
\|M_f\|=\|[f]\|=p_{\mathrm{loc}}(f).
$$

Here $p_{\mathrm{loc}}$ is a seminorm on source functions and a norm after quotienting. Semifinite reduction repairs visibility. Localizability is the criterion for the associated duality and von Neumann-algebraic conclusions; a localizable realization, when needed, is a separate construction.

# Limits

- A general GQG has no algebraic kernel unless its observations carry suitable structure.
- A general injective observation need not preserve magnitude.
- Exact GQG v0.1 does not model noise, power, tolerance, or approximate equivalence.
- Witness-relative equivalence does not prove source identity or ontological nonexistence.
- The formalism entails no interpersonal, political, psychological, economic, or metaphysical conclusion.

# First law

$$
\boxed{
\begin{gathered}
\text{No quotient identification}\\
\text{without a declared observation system.}
\end{gathered}
}
$$

**Present -> Declare witnesses -> Observe -> Quotient -> Prove descent -> Compose.**

Complete only under a separately declared completion notion.

---

**Status:** working corecard for GQG v0.1.  
**License:** CC0 1.0 Universal.  
**Position:** proposed organizing framework built from established mathematics.
