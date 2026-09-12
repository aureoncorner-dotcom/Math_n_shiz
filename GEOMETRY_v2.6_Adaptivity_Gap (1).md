# GEOMETRY v2.6 increment — unbounded batch/adaptive gap

Replace the v2.5 three-to-two sequential remark with a family whose adaptivity gap grows without bound. Batch hitting set and sequential acquisition stay different policy classes. Exact descent of \(W\) is held fixed.

## Instance \(D_n\)

Let \(n\ge 2\). Source domain \(D_n=\{1,2,\ldots,n\}\). Label \(\pi\) is constant. Target \(W(x)=x\).

Primitive coordinates are **threshold queries**. For each gap \(t\in\{2,3,\ldots,n\}\)

\[
c_t(x)=\mathbf 1[x\ge t]\in\{0,1\}.
\]

These \(n-1\) functions are pairwise distinct as maps \(D_n\to\{0,1\}\). Any other cut \(x\ge\tau\) with \(\tau\in\mathbb R\) coincides with one of them or is constant. Unit costs \(a_t=1\). The label is known before acquisition (one fiber). Queries do not change the state.

Bad pairs: every \(\{x,y\}\) with \(x\neq y\). The separating set of a consecutive pair \(\{i,i+1\}\) is the singleton \(\{c_{i+1}\}\). A non-consecutive pair \(\{i,j\}\), \(j\ge i+2\), is separated by every \(c_t\) with \(i<t\le j\).

## Batch theorem

Every hitting set of \(H=\{\,S_{xy}:x\neq y\,\}\) contains \(\{c_2,\ldots,c_n\}\).

**Proof.** The family \(H\) contains the \(n-1\) singletons \(S_{i,i+1}=\{c_{i+1}\}\). A hitting set must pick the unique member of each singleton. Those members are all distinct, so the unique inclusion-minimal (and unique minimum-cardinality, unique minimum-cost) batch is the full menu. Hence

\[
C_{\mathrm{fixed}}(D_n)=C_{\mathrm{label,worst}}(D_n)=n-1.
\]

No proper subset of thresholds makes \(W\) descend through \((\pi,(c_t)_{t\in J})\): the missed consecutive pair remains a same-label, different-\(W\) collision.

## Adaptive theorem

There is a sequential policy that uses at most \(\lceil\log_2 n\rceil\) threshold queries in the worst case and returns \(W(x)\).

**Proof.** Binary search on the chain. Maintain an interval \(L\le x\le R\), start \(L=1\), \(R=n\). While \(L<R\), query \(c_t\) at \(t=\lfloor(L+R+1)/2\rfloor\) (a legal menu threshold). If \(c_t(x)=1\) set \(L=t\), else set \(R=t-1\). Each step strictly shrinks the interval. At most \(\lceil\log_2 n\rceil\) steps leave \(L=R=x\). The policy is causal: the next index depends only on answers already in hand. Correctness is ordinary binary search on a total order.

Information lower bound: \(n\) possible values of \(W\), each query has two answers, so \(\lceil\log_2 n\rceil\) is also necessary in the worst case among adaptive threshold policies. The policy is optimal in that class.

## Gap

\[
\frac{C_{\mathrm{fixed}}(D_n)}{\text{adaptive worst-case queries}}
=\frac{n-1}{\lceil\log_2 n\rceil}\to\infty
\qquad(n\to\infty).
\]

v2.5’s eight-triple example gave the constant ratio \(3/2\). That example remains correct and remains the right warning that batch formulae are not the sequential optimiser. It does not exhibit an unbounded factor. \(D_n\) does.

## What this does not change

- Feasibility still precedes expectation. One fiber, fully listed.
- Inventory of the adaptive policy, if inventory means “hold every threshold the policy *might* query,” is still \(n-1\). Per-case query count is \(\lceil\log_2 n\rceil\). Those are different objectives; v2.5 already separated them.
- Fully sequential class is larger than one-batch-after-\(q\). This increment only enlarges the *documented gap* between those classes.
- Threshold menu is part of the declaration. If the menu is restricted to \(k<\log_2 n\) thresholds, neither class identifies every \(x\).
- Not a claim about human timing, service \(\pi_{\mathrm{DS}}\), TD-COS-FH-001, or foreign imports.
- Status board inherited from v2.5 is untouched.

## Drop-in replacement sentence for §5.1

Delete the eight-triple paragraph as the sole sequential illustration. Keep it as a constant-ratio example if wanted. Add:

> On \(D_n=\{1,\ldots,n\}\), constant \(\pi\), \(W(x)=x\), and unit-cost thresholds \(c_t=\mathbf 1[x\ge t]\) for \(t=2,\ldots,n\), every exact batch uses all \(n-1\) thresholds, while binary search uses \(\lceil\log_2 n\rceil\) queries in the worst case. Sequential acquisition can beat every exact batch by an arbitrarily large factor. The batch formulae remain the exact optimiser only inside the one-batch-after-\(q\) class.

## Checks

Small \(n\): \(n=2\) both classes use \(1\); \(n=3\) batch \(2\), adaptive \(2\); \(n=4\) batch \(3\), adaptive \(2\); \(n=8\) batch \(7\), adaptive \(3\). Consecutive singletons in \(H\) are the only fact the batch side needs; they can be read off by hand for these \(n\).
