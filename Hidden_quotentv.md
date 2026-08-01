# The Hidden Quotient Behind the Multiplication Representation

A small point of notation in measure theory conceals one of the fundamental structural steps of functional analysis. Textbooks introduce $L^\infty(X,\mu)$, define multiplication operators

$$
M_f : L^2(X,\mu)\to L^2(X,\mu),
\qquad
(M_f g)(x) = f(x)\,g(x),
$$

and immediately identify the function $f$ with the operator $M_f$.

That identification is not primitive. It is the result of taking a quotient. Making the quotient explicit does three things. It isolates exactly which functions the Hilbert space cannot see. It replaces a norm identity that is false for general measures with the correct one. And it shows that the multiplication representation theorem and the duality $(L^1)^*\cong L^\infty$ are two manifestations of a single construction.

---

## 1. Begin with actual functions

Rather than beginning with equivalence classes, let

$$
B(X,\Sigma)
=
\{\,f : X \to \mathbb{C} \;:\; f \text{ measurable and bounded}\,\},
$$

equipped with the ordinary supremum norm. This is already a commutative unital $C^*$-algebra.

Starting here avoids a common source of confusion. The phrase "essentially bounded" already involves an almost-everywhere notion, whereas $B(X,\Sigma)$ consists of honest functions. No identification has yet been made.

---

## 2. The multiplication representation

Define

$$
\pi : B(X,\Sigma) \longrightarrow B\big(L^2(X,\mu)\big),
\qquad
\pi(f) = M_f.
$$

The map is linear and multiplicative, preserves adjoints, and sends the constant function $1$ to the identity:

$$
M_{fg} = M_f M_g,
\qquad
M_{\overline f} = M_f^{\,*},
\qquad
M_1 = I.
$$

Thus $\pi$ is a unital $*$-homomorphism. It is moreover contractive:

$$
\|M_f g\|_2^2 = \int |f|^2\,|g|^2 \, d\mu \;\le\; \|f\|_\infty^2 \, \|g\|_2^2,
\qquad\text{so}\qquad
\|\pi(f)\| \le \|f\|_\infty.
$$

(Contractivity is automatic for any $*$-homomorphism between $C^*$-algebras, but here it is visible by hand.) Record the consequence now: $\ker\pi$ is a **closed**, self-adjoint, two-sided ideal of $B(X,\Sigma)$ — closed because $\pi$ is continuous, self-adjoint because $M_{\overline f} = M_f^{\,*}$, an ideal because $M_{gf} = M_g M_f$. This will matter in §4.

---

## 3. The hidden kernel

At this point most expositions quietly write

> "$M_f = 0$ iff $f = 0$ almost everywhere."

This is true under the standing hypotheses of introductory texts — $\sigma$-finiteness, for instance — and false for arbitrary measures. For a general measure space the correct statement is

$$
\ker\pi
=
\{\, f : f = 0 \ \text{locally almost everywhere} \,\},
$$

meaning $f = 0$ a.e. on every measurable set of finite measure.

**Proof.** Suppose $M_f = 0$. If $E \in \Sigma$ with $\mu(E) < \infty$, then $\chi_E \in L^2(X,\mu)$, and

$$
0 = M_f\chi_E = f\chi_E,
$$

so $f = 0$ a.e. on $E$.

Conversely, suppose $f = 0$ locally a.e., and let $g \in L^2$. Then

$$
\{|g|>0\} = \bigcup_{n\ge 1}\{|g|\ge 1/n\},
$$

and Chebyshev's inequality gives

$$
\mu\{|g|\ge 1/n\} \le n^2\,\|g\|_2^2 < \infty.
$$

So every $L^2$-function is carried, modulo a null set, by a countable union of finite-measure sets. On each of these $f$ vanishes a.e.; hence $fg = 0$ a.e. and $M_f = 0$. $\blacksquare$

Note the asymmetry the proof exposes: $L^2(\mu)$ only ever probes the $\sigma$-finite part of the space. Everything that follows flows from this.

**An example where the two notions differ.** Let

$$
X = [0,1] \sqcup \{p\},
\qquad
\mu = \text{Lebesgue measure on } [0,1],
\qquad
\mu(\{p\}) = \infty.
$$

Any measurable set containing $p$ has infinite measure, so every finite-measure set lies inside $[0,1]$; and any $g$ with $g(p)\ne 0$ has $\int |g|^2\,d\mu = \infty$. Hence, canonically,

$$
L^2(X,\mu) \cong L^2[0,1]:
$$

the point $p$ is invisible to the Hilbert space. Now take $f = \chi_{\{p\}}$. Then $M_f = 0$, although $f$ is *not* zero almost everywhere — $\{f\ne 0\} = \{p\}$ has infinite, in particular nonzero, measure. So $f$ is locally null but not null, and $\ker\pi$ strictly contains the null functions. The measure is not semifinite: $\{p\}$ has positive measure but no measurable subset of finite positive measure.

Keep this example in hand; it returns in §5.

---

## 4. The quotient

Since $\ker\pi$ is a closed self-adjoint ideal, the quotient

$$
B(X,\Sigma)\big/\ker\pi
$$

is again a $C^*$-algebra under the quotient norm, and the First Isomorphism Theorem — in its $C^*$-algebraic form — yields an induced representation

$$
\overline\pi :
B(X,\Sigma)/\ker\pi
\longrightarrow
B\big(L^2(X,\mu)\big)
$$

which is injective/faithful (for $*$-homomorphisms the two words are synonyms).

This is the first place where one may legitimately identify

$$
[f]
\quad\longleftrightarrow\quad
M_f.
$$

The quotient is what removes the ambiguity. No quotient, no faithful representation.

---

## 5. Faithful, hence isometric: the correct norm identity

Two different statements are often conflated. The quotient makes $\overline\pi$ injective. A separate theorem of $C^*$-algebra theory — not a consequence of the isomorphism theorem — says that every injective $*$-homomorphism between $C^*$-algebras is automatically isometric. Combining them:

$$
\|M_f\|
=
\big\|[f]\big\|_{B/\ker\pi}
=
\inf_{h\in\ker\pi}\|f+h\|_\infty
=
\|f\|_{\infty,\mathrm{loc}},
$$

where

$$
\|f\|_{\infty,\mathrm{loc}}
=
\inf\{\, c\ge 0 : \{|f|>c\} \text{ is locally null} \,\}
$$

is the **locally essential supremum**. The last equality is elementary: if $\{|f|>c\}$ is locally null, then $h = -f\,\chi_{\{|f|>c\}}$ lies in $\ker\pi$ and $\|f+h\|_\infty \le c$; conversely, $\|f+h\|_\infty \le c$ forces $\{|f|>c\} \subseteq \{h\ne 0\}$, a locally null set.

Two consequences.

First, the familiar textbook identity

$$
\|M_f\| = \operatorname*{ess\,sup}_{\mu} |f|
$$

is not a theorem of general measure theory; it is a semifinite phenomenon. In the example of §3,

$$
\operatorname{ess\,sup}\,|\chi_{\{p\}}| = 1,
\qquad
\|M_{\chi_{\{p\}}}\| = 0.
$$

The identity that holds for every measure is $\|M_f\| = \|f\|_{\infty,\mathrm{loc}}$, and the present framework produces it for free.

Second, the logical order is

$$
\text{quotient}
\;\Longrightarrow\;
\text{faithful}
\;\Longrightarrow\;
\text{isometric},
$$

with the last implication a theorem of $C^*$-theory.

---

## 6. The semifinite collapse

Suppose $\mu$ is semifinite: every measurable set of positive measure contains a subset of finite positive measure. Then locally null sets are null — if $\{f\ne 0\}$ had positive measure, it would contain a subset of finite positive measure on which $f$ could not vanish a.e. Hence

$$
f = 0 \ \text{locally a.e.}
\iff
f = 0 \ \text{a.e.},
$$

so $\ker\pi = \{f = 0 \text{ a.e.}\}$, and the quotient becomes the familiar space

$$
L^\infty(X,\mu)
=
B(X,\Sigma)\big/\{f = 0 \text{ a.e.}\},
$$

with quotient norm the ordinary essential supremum. The standard presentation — including the standard norm identity — is recovered. The hidden quotient has simply been built into the definition.

---

## 7. The semifinite reduction: what the Hilbert space sees

For a general measure, which familiar object is $B(X,\Sigma)/\ker\pi$? The answer is the $L^\infty$ of the **semifinite reduction** of $\mu$:

$$
\mu_{\mathrm{sf}}(E)
=
\sup\{\,\mu(F) : F\subseteq E,\ F\in\Sigma,\ \mu(F)<\infty\,\}.
$$

Four routine verifications:

$\mu_{\mathrm{sf}}$ is a measure, $\mu_{\mathrm{sf}}\le\mu$, with equality on every set of finite $\mu$-measure. It is semifinite, and $\mu$ is semifinite iff $\mu = \mu_{\mathrm{sf}}$.

A set is $\mu_{\mathrm{sf}}$-null iff it is locally $\mu$-null: $\mu_{\mathrm{sf}}(E) = 0$ iff every finite-$\mu$-measure subset of $E$ is $\mu$-null iff $\mu(E\cap F) = 0$ for every finite-measure $F$. Hence

$$
\mathcal N_{\mu_{\mathrm{sf}}}
=
\mathcal N_{\mathrm{loc}}.
$$

Every set $E$ of finite $\mu_{\mathrm{sf}}$-measure decomposes as $E = F \sqcup N$ with $\mu(F) = \mu_{\mathrm{sf}}(E) < \infty$ and $N$ locally null. (Take nested $F_k\subseteq E$ with $\mu(F_k)\uparrow\mu_{\mathrm{sf}}(E)$ and put $F = \bigcup_k F_k$; a subset $G\subseteq E\setminus F$ with $0<\mu(G)<\infty$ would give $\mu(F\cup G) > \mu_{\mathrm{sf}}(E)$, a contradiction.)

Every $\mu_{\mathrm{sf}}$-essentially-bounded class contains a bounded representative — truncate at the essential bound; the modification occurs on a $\mu_{\mathrm{sf}}$-null set.

The last two points give an isometric $*$-isomorphism

$$
B(X,\Sigma)\big/\ker\pi
\;\cong\;
L^\infty(\mu_{\mathrm{sf}}),
$$

the quotient norm on the left being exactly the $\mu_{\mathrm{sf}}$-essential supremum, i.e. the locally essential supremum $\|\cdot\|_{\infty,\mathrm{loc}}$ of §5.

Moreover the Hilbert space cannot tell $\mu$ from $\mu_{\mathrm{sf}}$. By the argument of §3, every $L^p(\mu)$-class ($p<\infty$) is carried by a countable union of finite-$\mu$-measure sets, on which the two measures agree; and by the decomposition above, every finite-$\mu_{\mathrm{sf}}$-measure set is a finite-$\mu$-measure set plus locally null debris. Hence, canonically,

$$
L^p(\mu) = L^p(\mu_{\mathrm{sf}}),
\qquad
1\le p<\infty.
$$

Assembling the pieces: for an *arbitrary* measure space, the multiplication representation, once the quotient is taken, is exactly the standard representation of a semifinite space —

$$
B(X,\Sigma)
\;\twoheadrightarrow\;
L^\infty(\mu_{\mathrm{sf}})
\;\hookrightarrow\;
B\big(L^2(\mu_{\mathrm{sf}})\big)
=
B\big(L^2(\mu)\big).
$$

Every measure acts on its own $L^2$ as if it had been semifinitely reduced first. The quotient of §4 is the algebraic shadow of that reduction. (In the example of §3, $\mu_{\mathrm{sf}}$ is Lebesgue measure on $[0,1]$ extended by $\mu_{\mathrm{sf}}(\{p\}) = 0$.)

---

## 8. Localizability: the structural theorem

One question remains: when is the represented algebra everything one wants it to be — the dual of $L^1$, and a von Neumann algebra? Neither is automatic, even after the quotient. Both are governed by a single condition on the *reduced* measure.

Throughout, "localizable" is used in Fremlin's sense — semifinite, with Dedekind complete measure algebra — so that "semifinite and localizable" would be redundant. Since $\mu_{\mathrm{sf}}$ is automatically semifinite, the condition below amounts precisely to Dedekind completeness of the Boolean algebra $\Sigma/\mathcal N_{\mathrm{loc}}$.

There is always a canonical map

$$
B(X,\Sigma)/\ker\pi
\longrightarrow
\big(L^1(X,\mu)\big)^*,
\qquad
[f]
\longmapsto
\Big( g \mapsto \int fg \, d\mu \Big),
$$

and it is always isometric. The upper bound $\big|\int fg\,d\mu\big| \le \|f\|_{\infty,\mathrm{loc}}\,\|g\|_1$ holds because $L^1$-functions, like $L^2$-functions, are carried by countable unions of finite-measure sets, on which $|f| \le \|f\|_{\infty,\mathrm{loc}}$ a.e.; it is attained in the limit by testing against $g = \chi_A\,\overline{f}/|f|$ with $A \subseteq \{|f|>c\}$ of finite positive measure and $c < \|f\|_{\infty,\mathrm{loc}}$. (Contrast the classical formulation: from $L^\infty(\mu)$, i.e. modulo null sets only, the map is injective iff $\mu$ is semifinite. Injectivity fails exactly when one has not quotiented enough. From $B/\ker\pi$ it never fails.) Localizability is exactly what makes the map onto. Precisely:

**Theorem.** For an arbitrary measure space $(X,\Sigma,\mu)$, the following are equivalent.

1. $\mu_{\mathrm{sf}}$ is localizable — equivalently, $\Sigma/\mathcal N_{\mathrm{loc}}$ is Dedekind complete.
2. The canonical isometry $B(X,\Sigma)/\ker\pi \to (L^1(\mu))^*$ is onto; that is, $(L^1(\mu))^* \cong L^\infty(\mu_{\mathrm{sf}})$ isometrically.
3. $\overline\pi\big(B(X,\Sigma)/\ker\pi\big)$ is a von Neumann algebra on $L^2(\mu)$.
4. $\overline\pi\big(B(X,\Sigma)/\ker\pi\big)$ is a maximal abelian $*$-subalgebra of $B(L^2(\mu))$.

Under any — hence all — of these conditions, $L^\infty(\mu_{\mathrm{sf}})$ is order complete as a lattice and is *the* commutative von Neumann algebra of the measure space, simultaneously realizing the $L^1$–$L^\infty$ duality.

This is the climax of the construction. The representation theorem and the duality theorem are not neighbors; they are the same quotient viewed through two pairings — against $L^2$ vectors on one side, against $L^1$ densities on the other. And when the equivalent conditions fail, they fail together: the duality map misses part of $(L^1)^*$ and the multiplication algebra fails to be weakly closed for the same underlying reason, suprema missing from $\Sigma/\mathcal N_{\mathrm{loc}}$.

---

## 9. The role of $\sigma$-finiteness

Why is none of this visible in a first course? Because $\sigma$-finiteness —

$$
X = \bigcup_{n=1}^{\infty} E_n,
\qquad
\mu(E_n) < \infty
$$

— implies both semifiniteness and localizability. The quotient silently reduces to "modulo null sets," *and* all the conditions of the structural theorem hold. Several logically distinct simplifications occur simultaneously, and the seams disappear.

One caution in the other direction: $\sigma$-finiteness does *not* imply separability of $L^1$ or $L^2$. Separability additionally requires the measure algebra to be countably generated modulo null sets. Classical treatments often assume both properties at once, compounding the collapse further.

---

## Summary

The multiplication representation is not faithful because multiplication operators are intrinsically injective. It becomes faithful only after quotienting by the functions the Hilbert space cannot see. For an arbitrary measure space the fundamental construction is

$$
B(X,\Sigma)
\longrightarrow
B(X,\Sigma)\big/\{\text{locally null functions}\}
\;\cong\;
L^\infty(\mu_{\mathrm{sf}})
\longrightarrow
B\big(L^2(X,\mu)\big),
$$

faithful — hence isometric — after the quotient, with the correct norm identity $\|M_f\| = \|f\|_{\infty,\mathrm{loc}}$.

Under semifiniteness the quotient is the familiar $L^\infty(X,\mu)$ and the familiar norm identity returns. Under localizability of $\mu_{\mathrm{sf}}$, the represented algebra is simultaneously the dual of $L^1(\mu)$ and the maximal abelian von Neumann algebra of the measure space: the multiplication representation theorem and the $L^1$–$L^\infty$ duality theorem are two manifestations of one quotient.

The standard textbook presentation is therefore not incorrect — it simply begins after the quotient has already been performed. Making the quotient explicit reveals the logical structure underlying the representation theory, the duality, and the passage to commutative von Neumann algebras, and it locates exactly where each classical simplification enters: the quotient trivializes at semifiniteness, completeness arrives with localizability, countability with $\sigma$-finiteness.

---

## Notes on the literature

**Cohn** is more than a general anchor here: he constructs $L^\infty$ explicitly as bounded measurable functions modulo local-a.e. equality and proves the canonical map into $(L^1)^*$ is always isometric. See D. L. Cohn, *Measure Theory*, 2nd ed., Birkhäuser, 2013, §§3.3 and 3.5.

**Segal** is the classical source for the semifinite case of the structural theorem — localizability $\iff (L^1)^*\cong L^\infty$ $\iff$ the multiplication algebra is maximal abelian: I. E. Segal, "Equivalences of measure spaces," *Amer. J. Math.* **73** (1951), 275–313.

**Fremlin** develops the semifinite version $\mu_{\mathrm{sf}}$ of a measure and the localizability conventions used above (under his definitions, "localizable" already includes semifiniteness): D. H. Fremlin, *Measure Theory*, vol. 2, esp. §§211, 213, and 243G for the duality.

**De Pauw** treats the arbitrary-measure surjectivity condition explicitly, under the name *semilocalizability*, characterizing it by order completeness of the Boolean algebra of measurable sets modulo locally null sets: T. De Pauw, "Undecidably semilocalizable metric measure spaces," *Commun. Contemp. Math.* **26** (2024), no. 4 (arXiv:1909.10190).

**Blecher–Goldstein–Labuschagne** give the modern operator-algebraic account of the full cycle of equivalences between localizable measure algebras, $L^\infty$-spaces, and abelian von Neumann algebras: D. P. Blecher, S. Goldstein, L. E. Labuschagne, "Abelian von Neumann algebras, measure algebras and $L^\infty$-spaces," *Expo. Math.* **40** (2022), 758–818, esp. Theorem 5.2.

---

**License:** CC0 1.0 Universal. To the extent possible under law, the author has waived all copyright and related or neighboring rights to this work. No attribution required. <https://creativecommons.org/publicdomain/zero/1.0/>
