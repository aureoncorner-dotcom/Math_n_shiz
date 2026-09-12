# Geometry of Typed Defects
## Working increment v0.2 — 11 September 2026
CC0 • Anonymous

Status: formal geometric extension of New geometry §§13–15 and GEOMETRY + GQG Working Master §§1–2.
Does not alter: chemistry freeze, Hidden Quotient v1.7 theorem, 39-screen algebra, toroidal Markov theorem, L=3 PASS, or any empirical status label.

Organizing addition: the non-descent locus is one set. Defects are not one kind. Distinguishing kinds is how the geometry improves without inventing a shape the no-shape lemma forbids.


## 0 Standing objects

Declared source domain \(D\), total retained map \(\pi:D\to Q=\pi(D)\), witness \(W:D\to Y\).

\[
N_W(\pi)=\bigl\{q\in Q:\exists x,y\in\pi^{-1}(q),\ W(x)\ne W(y)\bigr\}.
\]

Sector space \(\mathsf S_W(\pi)=\operatorname{im}(\pi,W)\). Canonical refinement \(\pi_W(x)=(\pi(x),W(x))\). Fiber diameter \(\delta_W(q)=\operatorname{diam} W(\pi^{-1}(q))\) when \(Y\) is metric.

No-shape lemma remains in force: any subset of \(Q\) can occur as \(N_W(\pi)\). Nothing below assigns a default topology to \(N_W\).


## 1 Calculus of loci

These are set identities. They do not require topology.

### 1.1 Product of witnesses

Let \(W=(W_1,W_2):D\to Y_1\times Y_2\).

**Lemma D1.** \(N_{(W_1,W_2)}(\pi)=N_{W_1}(\pi)\cup N_{W_2}(\pi)\).

Proof. A fiber is heterogeneous for the pair iff it is heterogeneous for at least one factor. \(\square\)

Corollary. Joint recovery fails exactly on the union of the separate defects. Cleaning one witness does not clean the other.

### 1.2 Coarsening the witness

Let \(f:Y\to Z\) and set \(W'=f\circ W\).

**Lemma D2.** \(N_{W'}(\pi)\subseteq N_W(\pi)\).

Proof. Distinct \(W'\) values require distinct \(W\) values. \(\square\)

A coarser question can descend after a finer question has already failed. This is the exact reading of New geometry §5: \(E_{\rm opt}\) may descend while \((E_g,E_b)\) does not. It is also the exact reading of §15.1: the existential Semaev relation can descend while specified signed output does not.

### 1.3 Refining the observation

If \(\pi=r\circ\pi'\) with \(\pi':D\to Q'\), then already (New geometry Prop. 14.4)

\[
r\bigl(N_W(\pi')\bigr)\subseteq N_W(\pi).
\]

**Lemma D3 (no new coarse defect).** If \(q\notin N_W(\pi)\), then no point of \(r^{-1}(q)\) lies in \(N_W(\pi')\).

A refinement can split a bad fiber. It cannot invent a collision whose coarse image was clean.

### 1.4 Restricting the domain

Let \(C\subseteq D\) and write \(\pi|_C\), \(W|_C\).

**Lemma D4.** \(N_{W|_C}(\pi|_C)\subseteq N_W(\pi)\cap\pi(C)\).

The inclusion can be strict. A collision that used a point of \(D\setminus C\) disappears. This is not descent on \(D\). It is descent on a smaller source. Record the restriction separately (Working Master §2; New geometry §15.3).

### 1.5 Predictive locus is a static locus

Let \(U:D\to D\) be a declared deterministic update.

**Lemma D5.** An autonomous retained update on \(Q\) exists if and only if \(N_{\pi\circ U}(\pi)=\varnothing\).

Proof. \(\pi(x)=\pi(y)\) implies \(\pi(Ux)=\pi(Uy)\) iff \(\pi\circ U\) is constant on every \(\pi\)-fiber iff that non-descent locus is empty. \(\square\)

Finite-horizon loss \(\delta_h^B\) is a metric strengthening of the same idea with witness equal to the \(h\)-step output law (or output sequence). Increasing \(h\) cannot shrink \(\delta_h^B\). Matching a coarser output \(B\) at one step is \(N_B(\pi)=\varnothing\), which does not imply \(N_{\pi\circ U}(\pi)=\varnothing\).

The Sophie Germain example is D5, not a new closure theorem: \(r(3)=r(5)\) while \(r(U(3))\ne r(U(5))\), so \(3,5\) witness \(N_{r\circ U}(r)\ne\varnothing\).


## 2 Five defect kinds

Each kind has a test, a repair that is legal for that kind, and a repair that is illegal.

### Kind I — Operation loss on a surviving relation

Test. Two maps \(W_{\rm out}\) and \(W_{\rm rel}\) on the same \(D\), with \(N_{W_{\rm rel}}(\pi)=\varnothing\) and \(N_{W_{\rm out}}(\pi)\ne\varnothing\).

Legal repair. Retain the extra coordinate that splits the \(W_{\rm out}\) fiber (e.g. the sign/\(y\)-coordinate).

Illegal repair. Treat vanishing of \(W_{\rm rel}\) as recovery of \(W_{\rm out}\).

Instance. New geometry §15.1. On affine pairs of \(E(\mathbb F_{13}):y^2=x^3+2x+2\) with affine sum, \(\pi(P,Q)=(x(P),x(Q))\) loses \(x(P+Q)\) at \((P,Q)\) versus \((P,-Q)\), while the Semaev relation \(S_3(x_1,x_2,x_3)=0\) still records existence of some signs. Existential relation and specified output are different witnesses. Lemma D2 says the coarser one can descend.

### Kind II — Unit / character loss

Test. \(\pi\) factors through an ideal class, a norm, or another map that kills a unit group, and \(W\) is a logarithm or character that sees that unit.

Legal repair. Add a character of declared rank, kernel, modulus, and precision (Schirokauer-type local log on a stated two-element domain, or the full map under its own hypotheses).

Illegal repair. Promote a coefficient that separates one pair into a global recovery theorem. Illegal also: treat \(\gcd(h,\ell)=1\) as optional when writing \(h^{-1}\bmod\ell\).

Instance. New geometry §15.2. In \(\mathbb Z[\sqrt{2}]\), \((1)=(1+\sqrt{2})\) as ideals; reduction \(\sqrt{2}\mapsto 3\) into \(\mathbb F_7\) gives distinct base-3 logs modulo 3. The local character \(L\) separates that pair. Pair separation is not Leopoldt, not unit-rank sufficiency on a larger domain, and not NFS-DL.

### Kind III — Subgroup-relative injectivity

Test. A homomorphism \(\varphi:G\to H\) and a declared subgroup \(C\le G\) satisfy \(\ker\varphi\cap C=\{e\}\) while \(\ker\varphi\ne\{e\}\).

Legal repair. Restrict the source to \(C\) and record the restriction (Lemma D4).

Illegal repair. Infer injectivity on \(G\), infer a computational speedup, or identify this with Weil restriction / GHS / Jacobian HCDLP. Those are separate assertions.

Instance. New geometry §15.3.

### Kind IV — Discrete sector defect on disconnected fibers

Test. \(A_W=dW|_{\ker d\pi}=0\) on every connected component of a fiber, yet the componentwise constants disagree.

Legal repair. Retain a discrete sheet label, or pass to \(\mathsf S_W\).

Illegal repair. Treat a vanishing vertical differential as descent when fibers are not connected (New geometry Thm 14.7 converse fails).

### Kind V — Representability gap outside the image

Test. \(\pi\) is injective on the declared domain, so \(N_W(\pi)=\varnothing\), but an object needed by a larger question does not lie in \(\operatorname{im}\pi\).

Legal repair. Name the missing object and enlarge the codomain or the observation (Hidden Quotient example C; point evaluation in example A is a different repair — there \(N_W\) was the whole of \(Q\)).

Illegal repair. Call the gap \(N_W(\pi)\). Non-descent is a collision inside an attained fiber. A missing dual functional is outside the image.

These five kinds are not a partition of every possible failure. They are the kinds the present corpus actually uses. A new example must say which kind it is, or declare a sixth.


## 3 What may be identified, and what may not

| Object A | Object B | Identify? |
|---|---|---|
| \(N_W(\pi)=\varnothing\) | existence of \(\bar W:Q\to Y\) | Yes (Thm 14.2) |
| \(N_{\pi\circ U}(\pi)=\varnothing\) | autonomous retained update | Yes (Lemma D5) |
| \(N_{W'}(\pi)=\varnothing\) for \(W'=f\circ W\) | \(N_W(\pi)=\varnothing\) | No (D2 is only inclusion) |
| \(N_{W|_C}(\pi|_C)=\varnothing\) | descent on \(D\) | No (D4) |
| \(q\in N_W(\pi)\) | \(q\in\partial N_{W,\varepsilon}(\pi)\) | No (§14.8) |
| source-space transition | quotient-space boundary | No (§14.8; lithium pressure) |
| Kind I existential zero | Kind I specified output | No |
| Kind II pair character | global Schirokauer sufficiency | No |
| Kind V missing dual | Kind I/II fiber collision | No |
| combining projects | transferring proof | No (Working Master start-here rule) |


## 4 Sector space as the typed attachment

\(\mathsf S_W(\pi)\) already carries every attained pair \((q,y)\). Typed defects read off it as follows.

- Kind I/II/III/IV: some \(r\)-fiber of \(\mathsf S_W\to Q\) has more than one point.
- Which kind: look at what extra coordinate splits that fiber (sign, unit character, subgroup membership, sheet index).
- Kind V: \(\mathsf S_W\to Q\) is a graph of a function, and the defect lives in a different ambient map.

Canonical refinement \(\pi_W\) kills Kind I–IV for this particular \(W\) by retaining \(W\) itself. It does not select a mechanistic coordinate, does not bound dimension, and does not make a predictor available at runtime. That sentence is already in §14.3; it stays.

Context attachment is a map \(c:D\to C\) such that \(N_W((\pi,c))=\varnothing\) while \(N_W(\pi)\ne\varnothing\). An inclusion-minimal such \(c\), among a declared menu of available coordinates, is the empirical compiler’s \(S^*(W,D,C)\). Geometry supplies the test. It does not supply the menu.


## 5 Predictive stack, kept separate from static recovery

Declare, in this order:

1. Static witness \(W\) and its \(N_W(\pi)\).
2. Update or kernel \((U\) or \(P)\).
3. Predictive witness \(\pi\circ U\) or the next-observation law, and its locus (Lemma D5).
4. Horizon-\(h\) diameter \(\delta_h^B\) for a declared output \(B\).
5. Clock, if cross-time agreement fails while fixed-time agreement holds.

Do not feed future values of \(B\) into the present predictor. The \(\sim_\infty\) equivalence characterizes required information; it is not an admissible input list.

The 39-screen statements remain phase-rotation theorems on their declared circle. The toroidal all-orders theorem remains a theorem about \(Y_n=q(X_{dn})\) under TD-COS-FH-001. Neither is a special case of the other. Both instantiate D5 / finite-horizon loss with different \(D,U,W\).


## 6 First geometry gate, unchanged and now typed

A run still freezes \((D,W,\pi,d_Y,\varepsilon,\mathcal E)\). Add one field:

6. Defect kind, or “unclassified.”

Certified empirical non-descent remains a located pair with distance lower bound \(>\varepsilon\). Failure to find a pair is not cleanliness. Kind V cannot be certified by a same-fiber pair; it needs an explicit missing-object witness outside \(\operatorname{im}\pi\).


## 7 What this increment establishes

1. Product, coarsening, refinement, restriction, and predictive identification of loci (D1–D5).
2. Five named defect kinds matching the corpus, with legal and illegal repairs.
3. An identification table that prevents the arithmetic packet from collapsing into one “descent.”
4. Sector space as the attachment point for kinds I–IV; representability gaps kept outside \(N_W\).

It does not establish: a shape of \(N_W\) on any physical domain; holonomy of any empirical system; a smaller 39-screen phase; a change to Hidden Quotient v1.7; a cryptographic assessment; a chemistry un-freeze.

\[
\boxed{\text{TYPED DEFECT CALCULUS: ESTABLISHED}}
\]
\[
\boxed{\text{GLOBAL NON-DESCENT SHAPE: STILL NOT MEASURED}}
\]
\[
\boxed{\text{SOURCE FREEZES: UNCHANGED}}
\]


## 8 Use

Edit Working Master §1 with a one-line pointer: defect kinds and locus calculus live in this increment. Keep proofs here. Do not copy the arithmetic packet forward without the §15.5 qualifications (probable primality, Semaev resultant factors, prime-degree Weil restriction still has a base field, unit-character rank/kernel/precision, \(h^{-1}\) needs \(\gcd(h,\ell)=1\)).
