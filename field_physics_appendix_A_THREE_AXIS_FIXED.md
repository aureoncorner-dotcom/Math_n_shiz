Appendix A — Three-Axis Fixed-Holonomy Sector Construction

Status: Canonical finite-volume construction selected; execution validation pending
Scope: Q2 at h_6=0 only
Controlling rule: This appendix governs every odd-winding, charge-one-sector, and holonomy-dependent statement in the protocol. Where the pre-appendix body used f_{\rm odd} without an ensemble label, it is read as the fixed-holonomy quantity defined below. The fully link-summed periodic ensemble has no independently variable odd mod-two winding sector.

A.0 Gate and ensemble separation

The protocol uses two distinct finite-volume ensembles.

1. Z_{\rm full}: the original direct model with every Z_2 gauge link summed and periodic lattice identifications. Its exact dual projects onto trivial mod-two current homology. Z_{\rm full} remains the production ensemble for Q1, bulk thermodynamics, and the h_6=0 calibration of Q3.

2. Z_{\rm FH}: the three-axis fixed-trivial-holonomy ensemble defined in A.2. Its positive dual representation contains eight explicit current-homology sectors q\in Z_2^3. Z_{\rm FH} is the only ensemble in which the Q2 odd-winding statistic is defined.

No observable, universal crossing value, or fit amplitude may be transferred between Z_{\rm full} and Z_{\rm FH} without an explicit identity or a separately reported cross-ensemble comparison. Appending this construction does not by itself open Q2. The Q2 gate remains closed until every validation item in A.8 passes and its immutable validation record is hashed.

A.1 Frozen lattice geometry

Let \Lambda_L be the oriented L\times L\times L cubic cellulation of T^3. All coordinates are elements of {0,1,\ldots,L-1}, with addition modulo L. Positive link orientations are +\hat x,+\hat y,+\hat z.

Freeze the three positively oriented reference cycles

[
\Gamma_x=\{((x,0,0),\hat x):0\le x<L\},
]

[
\Gamma_y=\{((0,y,0),\hat y):0\le y<L\},
]

[
\Gamma_z=\{((0,0,z),\hat z):0\le z<L\}.
]

Let \Sigma_\alpha be the dual noncontractible cut orthogonal to \Gamma_\alpha, oriented so that the mod-two intersection pairing obeys

[
\langle\Sigma_\alpha,\Gamma_\beta\rangle=\delta_{\alpha\beta}\pmod2.
]

The ordered tuple (\Gamma_x,\Gamma_y,\Gamma_z), its base point, link ordering, cut convention, and orientation convention are part of the frozen geometry artifact. They may not be translated, rerouted, or selected after target data are opened. Predetermined translated-cycle checks are validation tests, not replacements for the canonical tuple.

A.2 Direct fixed-holonomy ensemble

For a gauge configuration \sigma_\ell=\pm1 define the three reference-cycle holonomies

[
H_\alpha(\sigma)=\prod_{\ell\in\Gamma_\alpha}\sigma_\ell\in\{+1,-1\}.
]

Write h=(h_x,h_y,h_z)\in Z_2^3 and require

[
H_\alpha(\sigma)=(-1)^{h_\alpha}.
]

The exact fixed-holonomy partition function is

[
\boxed{
Z_h
=
\sum_{\{\sigma\}}
\int[d\theta]\,
e^{-H[\theta,\sigma]}
\prod_{\alpha=x,y,z}
\mathbf 1\!\left[H_\alpha(\sigma)=(-1)^{h_\alpha}\right].
}
]

This projector equation, not an informal gauge choice, is the definition. Equivalently, one may gauge-fix a spanning tree in the union of the three reference cycles and retain one closure bit per cycle. Fixing those three closure bits to +1 gives h=0. Any code using that equivalent representation must reproduce the projector definition exactly.

The primary Q2 ensemble is

[
\boxed{Z_{\rm FH}=Z_{000}.}
]

The fully summed periodic partition function is recovered without approximation:

[
\boxed{Z_{\rm full}=\sum_{h\in Z_2^3}Z_h.}
]

A.3 Exact character expansion and dual sector formula

Use the Z_2 character identity

[
\prod_\alpha
\mathbf 1\!\left[H_\alpha=(-1)^{h_\alpha}\right]
=
\frac1{8}
\sum_{q\in Z_2^3}
(-1)^{h\cdot q}
\prod_\alpha H_\alpha^{q_\alpha}.
]

Let \Gamma q denote the mod-two 1-chain

[
\Gamma q=q_x\Gamma_x+q_y\Gamma_y+q_z\Gamma_z.
]

After the same matter-current expansion, plaquette expansion, rotor integration, and gauge-link sums used in Section 4, the exact fixed-holonomy dual is

[
\boxed{
Z_h
=
\frac{C}{8}
\sum_{q\in Z_2^3}
\sum_{\{M,I,n\}}
(-1)^{h\cdot q}
t^{\sum_pM_p}
\prod_\ell w_J(I_\ell)
\prod_i\mathcal I_{|n_i|}(h_6)
\prod_i\delta_{\mathbb Z}\!\left[(\nabla\!\cdot I)_i+6n_i\right]
\prod_\ell\delta_{\mathbb Z_2}\!\left[I_\ell+M_\ell+(\Gamma q)_\ell\right].
}
]

Here

[
M_\ell=(\partial M)_\ell=\sum_{p\supset\ell}M_p\pmod2,
]

and

[
w_J(I)=\mathcal I_{|I|}(J)
]

for the cosine branch, while

[
w_J(I)=e^{-I^2/(2J)}
]

for the Villain branch. At h_6=0, n_i=0 and \nabla\!\cdot I=0. At nonzero h_6 the exact neutrality condition \sum_i n_i=0 is retained, but no finite-h_6 Q2 production result is authorized by this appendix.

Define the nonnegative sector coefficients

[
\boxed{
\mathcal Z_q
=
C
\sum_{\{M,I,n\}}
t^{\sum_pM_p}
\prod_\ell w_J(I_\ell)
\prod_i\mathcal I_{|n_i|}(h_6)
\prod_i\delta_{\mathbb Z}\!\left[(\nabla\!\cdot I)_i+6n_i\right]
\prod_\ell\delta_{\mathbb Z_2}\!\left[I_\ell+M_\ell+(\Gamma q)_\ell\right].
}
]

Then

[
\boxed{
Z_h=\frac1{8}\sum_q(-1)^{h\cdot q}\mathcal Z_q,
\qquad
\mathcal Z_q=\sum_h(-1)^{h\cdot q}Z_h.
}
]

These are an eight-component Walsh-Hadamard transform and its inverse. Summing h projects q to zero:

[
\boxed{Z_{\rm full}=\mathcal Z_{000}.}
]

This equation is the precise reason the fully summed periodic dual cannot supply an independently fluctuating odd mod-two winding observable.

A.4 Winding parity and the Q2 observable

Let \bar I=I\bmod2. The fixed-holonomy parity constraint is

[
\bar I+\partial M+\Gamma q=0.
]

Pairing with a closed dual cut \Sigma_\alpha gives

[
\langle\Sigma_\alpha,\bar I\rangle
=
q_\alpha\pmod2,
]

because a closed cut has zero mod-two intersection with the boundary \partial M and unit intersection with its matching reference cycle. With the winding normalization of Section 6.1,

[
\boxed{q_\alpha=W_\alpha\pmod2.}
]

The axis-resolved fixed-holonomy odd fraction is therefore

[
\boxed{
f_{\rm odd}^{(\alpha)}(L)
=
P_{Z_{000}}(q_\alpha=1)
=
P_{Z_{000}}(W_\alpha\ \mathrm{odd})
=
\frac{\sum_{q:q_\alpha=1}\mathcal Z_q}{\sum_q\mathcal Z_q}.
}
]

The cubic primary summary is

[
\boxed{
f_{\rm odd}(L)=\frac13\sum_{\alpha=x,y,z}f_{\rm odd}^{(\alpha)}(L),
}
]

but all three axis-resolved values must also be reported. No axis may be discarded after inspection.

Let e_\alpha be the holonomy bit vector with a single 1 in direction \alpha. The independent partition-ratio identity is

[
\boxed{
f_{\rm odd}^{(\alpha)}(L)
=
\frac12\left(1-\frac{Z_{e_\alpha}}{Z_{000}}\right).
}
]

More generally, the complete sector distribution is reconstructed by

[
\boxed{
p(q)=\frac{\mathcal Z_q}{\sum_r\mathcal Z_r}
=
\frac1{8}\sum_h(-1)^{h\cdot q}\frac{Z_h}{Z_{000}}.
}
]

The h=0 dual has nonnegative weights and no sign problem. Nonzero-h dual expressions are used for exact transforms and independent ratio checks; they are not sampled by treating signed weights as probabilities.

A.5 Frozen Markov kernels

The h=0 Q2 target density is proportional to the nonnegative summand of \sum_q\mathcal Z_q. Every production chain stores M,I,q and verifies both \nabla\!\cdot I=0 and I+M+\Gamma q=0\pmod2 after every accepted move.

A.5.1 Cube move

Choose an elementary cube uniformly and toggle M_p on its six faces. I and q are unchanged. Because \partial^2=0, the parity constraint is preserved. For a symmetric proposal,

[
R_{\rm cube}=t^{\Delta N_M},
\qquad
P_{\rm acc}=\min(1,R_{\rm cube}).
]

A.5.2 Coupled plaquette-current move

Choose a plaquette p uniformly and an orientation s=\pm1 with equal probability. Toggle M_p and add the oriented unit boundary current s\,\partial p to I. The proposal preserves divergence and link parity. Its ratio is

[
R_{p,s}
=
t^{\Delta M_p}
\prod_{\ell\in\partial p}
\frac{w_J(I_\ell+s\,\varepsilon_{p\ell})}{w_J(I_\ell)},
]

with \varepsilon_{p\ell}=\pm1 from the frozen orientation convention and \Delta M_p=+1 for 0\to1, -1 for 1\to0.

A.5.3 Even-current worm

Choose a tail site uniformly and s=\pm1 with equal probability. In the extended ensemble create defects \pm2, move the head by choosing one of the six oriented neighboring links uniformly, and propose I_\ell\to I_\ell+2s\varepsilon on the traversed link with local Metropolis ratio w_J(I_\ell+2s\varepsilon)/w_J(I_\ell). The worm closes only when the head returns to the tail after at least one accepted step. A noncontractible route may change W_\alpha by an even integer. There is no production path-length cap or silent partial-worm truncation.

A.5.4 Closed membrane-sheet move

Choose one of the three orientations and one of its L translated noncontractible plaquette sheets uniformly, then toggle every M_p on that sheet. Since the sheet has no boundary, I and q are unchanged. Accept with

[
R_{\rm sheet}=t^{\Delta N_M}.
]

A.5.5 Three-axis sector move

For a sector-move attempt in the scheduled axis \alpha, choose s=\pm1 with equal probability and propose

[
q_\alpha\to q_\alpha\oplus1,
\qquad
I_\ell\to I_\ell+s\,\varepsilon_{\alpha\ell}
\quad(\ell\in\Gamma_\alpha),
]

with all other variables unchanged. The reference loop is closed, so divergence is preserved; both I\bmod2 and \Gamma q change on the same links, so parity is preserved.

For the cosine branch,

[
\boxed{
R_{\alpha,s}^{\cos}
=
\prod_{\ell\in\Gamma_\alpha}
\frac{\mathcal I_{|I_\ell+s\varepsilon_{\alpha\ell}|}(J)}
{\mathcal I_{|I_\ell|}(J)}.
}
]

For the Villain branch,

[
\boxed{
R_{\alpha,s}^{\rm V}
=
\exp\!\left[-\frac1{2J}
\sum_{\ell\in\Gamma_\alpha}
\left((I_\ell+s\varepsilon_{\alpha\ell})^2-I_\ell^2\right)
\right].
}
]

Accept with \min(1,R). The reverse proposal uses the same axis and -s, so proposal probabilities are equal and detailed balance follows directly. This global move is the canonical sector-changing kernel. Any later accelerated sector worm, umbrella scheme, or tempered insertion requires a formal protocol amendment, its own detailed-balance proof, new validation hashes, and a new blind resource forecast before target execution.

A.5.6 Production schedule

One Q2 macro-sweep contains L^3 cube attempts, 3L^3 coupled plaquette-current attempts, completed even worms until their cumulative accepted path length is at least 3L^3, one randomly selected closed-sheet attempt, and one sector-move attempt in each axis in a uniformly shuffled order. Proposal-width or bias adaptation is prohibited in production.

A.6 Reachability and known efficiency boundary

At the mod-two level, the coupled plaquette move generates changes by plaquette boundaries, the closed-sheet move spans the three noncontractible membrane homology classes, and the three sector moves span q\in Z_2^3. At fixed parity, the difference of any two admissible integer currents is an even divergence-free current. Contractible and noncontractible even worms generate that remaining current space. These statements establish finite-state reachability for any finite current cutoff used in enumeration.

They do not guarantee rapid mixing at production sizes. In a confined regime, suppression of q_\alpha=1 is physical; in either regime, a poor proposal can add algorithmic suppression. Q2 is therefore inadmissible unless the round-trip and autocorrelation requirements in A.8 pass. Failure is reported as Q2 UNRESOLVED — SECTOR MIXING NOT VALIDATED, not as evidence of confinement.

A.7 Relation to the CKT axial implementation

Coleman, Kuklov, and Tsvelik describe odd-current updates only along z under the condition u_z=1. On a periodic torus, setting every z link to +1 is not accepted here as a self-proving gauge choice: closure variables and residual holonomy must be retained explicitly.

The CKT-aligned comparator maps to this appendix only after the following reconstruction:

1. fix z-directed tree links but retain the periodic closure variable;
2. identify that closure variable with the frozen h_z bit;
3. identify the odd z-current update with the A.5.5 transformation of q_z and I on \Gamma_z;
4. keep q_x=q_y=0 only for the explicitly labeled one-axis comparator;
5. reproduce the z-sector transform, direct/dual enumeration, and published Villain benchmarks.

If the closure bit is fixed away, or odd z currents are admitted after all z-link projectors were already imposed, the implementation is a different conditioned ensemble and cannot provide the canonical Q2 result. CKT’s published numerical behavior remains a literature-validation target; it is not an inherited proof of ensemble equivalence.

A.8 Validation gates before execution freeze

Every item below is mandatory. A failure blocks the execution hash. No failed axis, translated-cycle check, parameter point, or lattice size may be removed after its result is known.

A.8.1 Algebra and invariant tests

1. Verify the eight projector characters and both Walsh-Hadamard identities exactly over Z_2.
2. Verify by machine-exact chain arithmetic that \partial^2=0, \langle\Sigma_\alpha,\Gamma_\beta\rangle=\delta_{\alpha\beta}, and q_\alpha=W_\alpha\bmod2.
3. For every proposal and every accepted state, assert \nabla\!\cdot I=0 and I+M+\Gamma q=0\pmod2. At finite h_6 validation points also assert \sum_i n_i=0.
4. Verify Z_{\rm full}=\mathcal Z_{000}; f_{\rm odd} is not computed from Z_{\rm full}.

A.8.2 Exhaustive and high-precision small-volume tests

1. Exhaustively enumerate the complete mod-two state space at L=2 for all eight h and q labels.
2. Perform weighted L=2 and L=3 checks for both cosine and Villain weights. If integer currents are truncated, choose I_{\max} from a certified omitted-tail bound below 10^{-12} for every reported partition ratio and observable.
3. Compare all eight directly defined Z_h values with all eight dual \mathcal Z_q values through both transforms. Require relative disagreement no larger than max(10^{-10},10 times the certified tail bound).
4. Verify nonnegativity of every reconstructed \mathcal Z_q and normalization \sum_q p(q)=1 to the same tolerance.
5. Compare energy derivatives, the exact direct/dual plaquette relation, winding moments, and sector probabilities under identical holonomy conventions.

A.8.3 Detailed balance and reachability tests

1. On the L=2 state graph with the frozen enumeration cutoff, verify \pi(x)P(x,y)=\pi(y)P(y,x) for every nonzero transition to relative tolerance 10^{-12}.
2. Use breadth-first graph traversal to show that every positive-weight state is reachable within each q sector and that the three sector moves connect all eight q sectors.
3. Run the same tests with proposal order reversed and with independent RNG seeds; invariant results must be bitwise identical where arithmetic is exact.

A.8.4 Limiting-case tests

1. J=0: I=0 and q=000 exactly, hence f_{\rm odd}^{(\alpha)}=0 in Z_{000}.
2. t=0 with J>0: Z_{\rm full} remains q=000 by projection, while Z_{000} permits q_\alpha=1 only with a noncontractible odd-current loop. The leading minimum-loop suppression must scale with [w_J(1)/w_J(0)]^L; a forced zero is a code failure.
3. t\to1 in the flat, trivial-holonomy sector: reproduce the ordinary periodic XY current model and its winding-parity distribution.
4. Sum the eight direct holonomy sectors and recover the fully summed periodic observables.

A.8.5 Independent ratio and symmetry tests

1. Determine Z_{e_\alpha}/Z_{000} independently of q-occupancy sampling by exact enumeration on L=2,3 and by a preregistered free-energy-ratio estimator on blind pilot lattices.
2. Require agreement with 1-2f_{\rm odd}^{(\alpha)} within three combined standard errors for every axis and pilot point.
3. At isotropic couplings, require the three axis-resolved f_{\rm odd}^{(\alpha)} estimates to agree with a global correlated symmetry-test p-value of at least 0.05.
4. Repeat the blind validation after translating the complete canonical cycle tuple by r_x=(\lfloor L/2\rfloor,0,0), r_y=(0,\lfloor L/2\rfloor,0), and r_z=(0,0,\lfloor L/2\rfloor). At every blind validation point, require a correlated four-placement consistency-test p-value of at least 0.05. Failure makes Q2 unresolved; the best-looking cycle may not be selected.

A.8.6 Mixing and round-trip gate

For every Q2 production parameter point and lattice size:

1. each axis must show at least 100 effective completed sector round trips 0\to1\to0 in the aggregate of the eight independent chains;
2. the indicator 1[q_\alpha=1] must have rank-normalized \widehat R<1.01 and effective sample size at least 1,000;
3. sector autocorrelation, acceptance, residence times, and the complete 8-state q transition matrix must be reported;
4. starting all chains in q=000 and starting them evenly across all eight q values must give compatible stationary estimates within three combined standard errors.

If a true sector is too rare to produce 100 round trips, the ratio estimator may establish a bound only if that bound and its stopping rule were frozen before target outputs were opened. Otherwise Q2 is unresolved.

A.8.7 CKT comparator

At the published Villain validation point, run the reconstructed one-axis comparator and the canonical three-axis ensemble. Reproduce the published bulk benchmark within declared uncertainty, verify the A.7 mapping identities, and report any difference between the comparator and canonical z-sector statistics. Agreement validates implementation; disagreement does not authorize changing the canonical ensemble.

A.9 Q2 reporting rule

All Q2 results carry the ensemble label Z_{000}. Subject also to Appendix B’s upper-confidence-bound size-admissibility rule:

[
f_{\rm odd}^{(\alpha)}\to0
\quad\Longleftrightarrow\quad
Z_{e_\alpha}/Z_{000}\to1
]

supports suppression of odd charge-one winding in direction \alpha, while

[
f_{\rm odd}^{(\alpha)}\to c_\alpha>0
\quad\Longleftrightarrow\quad
Z_{e_\alpha}/Z_{000}\to1-2c_\alpha<1
]

supports odd-current proliferation in that fixed-holonomy construction. A directional split, failed ratio identity, failed translated-cycle check, failed mixing gate, or L_{\max}<4\,\xi_{\rm conf}^{\rm UCB} yields Q2 INCONCLUSIVE. Z_{\rm full} cannot by itself support either Q2 verdict.

A.10 Freeze artifacts and provenance

Before the execution root may be created, the following immutable artifacts must exist and hash successfully:

1. Appendix A canonical text;
2. frozen geometry specification for \Gamma_\alpha,\Sigma_\alpha, indexing, and orientations;
3. code-level transition table and acceptance-ratio specification;
4. exact algebra/invariant test report;
5. L=2 and L=3 enumeration outputs with current-tail certificate;
6. eight-sector direct/dual transform table;
7. independent partition-ratio validation report;
8. detailed-balance and reachability report;
9. blind mixing and round-trip pilot outputs;
10. CKT axial-mapping comparator report;
11. source commit and build-environment manifest.

The provenance chain records the pre-appendix protocol hash, this Appendix A hash, Appendix B and any amendments, immutable pilot outputs, the resource forecast, and only then the execution-root hash. Calibration-only blind pilots do not constitute target execution, but their immutable outputs and hashes are part of the chain.

No selective removal rule: after any validation or forecast output is opened, no axis, cycle placement, lattice size, parameter point, kernel, or failed check may be silently removed. A change requires a dated formal amendment, a new hash, revalidation of every affected item, and a revised blind resource forecast.

[
\boxed{\text{EXECUTION HASH BLOCKED UNTIL A.8 AND APPENDIX B BOTH PASS.}}
]

CC0 1.0 Universal
To the extent permitted by law, this work is dedicated to the public domain under CC0 1.0 Universal.
No permission required. Copy it, modify it, test it, redistribute it, build on it, or tear it apart.
No ownership claim. No attribution required. No warranty.
Use freely.
