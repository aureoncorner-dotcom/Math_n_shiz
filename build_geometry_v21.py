#!/usr/bin/env python3
"""Build GEOMETRY Working Master v2.1 PDF."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, ListFlowable, ListItem, HRFlowable, Preformatted,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Italic", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-BoldItalic", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuMono", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"))

INK = HexColor("#1a1714")
MUTED = HexColor("#5c564e")
RULE = HexColor("#c9c1b4")
BAND = HexColor("#f3eee6")
ACCENT = HexColor("#6b3f1f")
BOX_BG = HexColor("#f7f3ec")
BOX_BD = HexColor("#d9d0c3")
HEADER_BG = HexColor("#2c261f")

OUT = "/home/workdir/artifacts/GEOMETRY_Working_Master_v2.1.pdf"


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(HEADER_BG)
    canvas.rect(0, letter[1] - 28, letter[0], 28, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("DejaVuSans", 8)
    canvas.drawString(54, letter[1] - 18, "GEOMETRY — Working Master v2.1")
    canvas.drawRightString(letter[0] - 54, letter[1] - 18, "Service-absorbed successor")
    canvas.setFillColor(RULE)
    canvas.rect(0, 0, letter[0], 28, fill=1, stroke=0)
    canvas.setFillColor(MUTED)
    canvas.setFont("DejaVu", 8)
    canvas.drawString(54, 12, "CC0 1.0  ·  11 September 2026")
    canvas.drawRightString(letter[0] - 54, 12, f"{doc.page}")
    canvas.restoreState()


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(
        name="CoverKicker", fontName="DejaVuSans", fontSize=9,
        textColor=ACCENT, leading=12, spaceAfter=6, tracking=1,
    ))
    s.add(ParagraphStyle(
        name="CoverTitle", fontName="DejaVu-Bold", fontSize=22,
        textColor=INK, leading=26, spaceAfter=8,
    ))
    s.add(ParagraphStyle(
        name="CoverSub", fontName="DejaVu-Italic", fontSize=11,
        textColor=MUTED, leading=15, spaceAfter=4,
    ))
    s.add(ParagraphStyle(
        name="Meta", fontName="DejaVu", fontSize=9,
        textColor=MUTED, leading=13, spaceAfter=10,
    ))
    s.add(ParagraphStyle(
        name="H1", fontName="DejaVu-Bold", fontSize=13,
        textColor=INK, leading=17, spaceBefore=16, spaceAfter=8,
    ))
    s.add(ParagraphStyle(
        name="H2", fontName="DejaVu-Bold", fontSize=11,
        textColor=ACCENT, leading=15, spaceBefore=12, spaceAfter=6,
    ))
    s.add(ParagraphStyle(
        name="Body", fontName="DejaVu", fontSize=10,
        textColor=INK, leading=14.2, spaceAfter=7, alignment=TA_JUSTIFY,
    ))
    s.add(ParagraphStyle(
        name="BodyLeft", fontName="DejaVu", fontSize=10,
        textColor=INK, leading=14.2, spaceAfter=7, alignment=TA_LEFT,
    ))
    s.add(ParagraphStyle(
        name="Note", fontName="DejaVu-Italic", fontSize=9.5,
        textColor=MUTED, leading=13, spaceAfter=8,
    ))
    s.add(ParagraphStyle(
        name="Eq", fontName="DejaVu", fontSize=10,
        textColor=INK, leading=16, alignment=TA_CENTER,
        spaceBefore=6, spaceAfter=8,
    ))
    s.add(ParagraphStyle(
        name="Banner", fontName="DejaVuMono", fontSize=8.5,
        textColor=INK, leading=13, leftIndent=8, rightIndent=8,
    ))
    s.add(ParagraphStyle(
        name="Cell", fontName="DejaVu", fontSize=8,
        textColor=INK, leading=11,
    ))
    s.add(ParagraphStyle(
        name="CellHead", fontName="DejaVuSans-Bold", fontSize=8,
        textColor=white, leading=11,
    ))
    s.add(ParagraphStyle(
        name="BulletBody", fontName="DejaVu", fontSize=10,
        textColor=INK, leading=13.5, leftIndent=12, spaceAfter=3,
    ))
    s.add(ParagraphStyle(
        name="FooterNote", fontName="DejaVu", fontSize=8,
        textColor=MUTED, leading=11,
    ))
    return s


def P(text, st, key="Body"):
    return Paragraph(text, st[key])


def make_table(headers, rows, col_widths, st):
    head = [Paragraph(h, st["CellHead"]) for h in headers]
    body = []
    for row in rows:
        body.append([Paragraph(c, st["Cell"]) for c in row])
    data = [head] + body
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("BACKGROUND", (0, 1), (-1, -1), BOX_BG),
        ("FONTNAME", (0, 0), (-1, 0), "DejaVuSans-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("GRID", (0, 0), (-1, -1), 0.3, BOX_BD),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BOX_BG, white]),
    ]))
    return t


def banner_box(lines, st):
    inner = [Paragraph(line, st["Banner"]) for line in lines]
    t = Table([[inner]], colWidths=[468])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BAND),
        ("BOX", (0, 0), (-1, -1), 0.6, ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def build():
    st = styles()
    story = []

    story.append(P("GEOMETRY SUCCESSOR CARD", st, "CoverKicker"))
    story.append(P("Working Master v2.1", st, "CoverTitle"))
    story.append(P("Service-absorbed successor. The quotient now has two witnesses and five lemmas.", st, "CoverSub"))
    story.append(P("11 September 2026  ·  CC0 1.0 Universal  ·  Anonymous", st, "Meta"))
    story.append(HRFlowable(width="100%", thickness=0.8, color=ACCENT, spaceAfter=12))

    story.append(P(
        "Successor to <i>GEOMETRY + GQG Working Master</i> (8 Sep 2026) and "
        "<i>Geometry Update for Direct Service and Ablation</i> v1 (9 Sep 2026). "
        "This card absorbs the service layer into the core without identifying state spaces "
        "or transferring proof status.",
        st,
    ))

    story.append(P("Claim boundary", st, "H1"))
    story.append(P(
        "This card records typed projections, exact factorizations on declared domains, "
        "and presentation-level ablation. It does not prove that a backend stage occurred, "
        "that a physical field exists, that a measure-space theorem is a social theorem, "
        "or that deleting a visible record reduced internal work.",
        st,
    ))
    story.append(banner_box([
        "EVENT ≠ CODE ≠ CLAIM",
        "internal necessity ≠ visible necessity",
        "presentation minimality  ⇏  predictive autonomy",
        "three geometric terms  ≠  three sovereign seats",
    ], st))
    story.append(Spacer(1, 8))
    story.append(P(
        "Finite identities stay finite. Missing coverage is UNRESOLVED. "
        "A located same-label / different-witness pair is FAILED descent for that witness.",
        st,
    ))

    story.append(P("0. What v2.1 actually changes", st, "H1"))
    story.append(P(
        "The 8–9 September sources already had the right question and the right caution. "
        "They did not have a single typed stack, named lemmas for the five service additions, "
        "or a proof that deletion-cost cannot live on the service quotient. v2.1 does that work and stops there.",
        st,
    ))
    story.append(make_table(
        ["Repair", "Why it matters"],
        [
            ["Two witnesses, one stack",
             "Audit W and service W_DS can disagree. The geometry already allowed this; the notation did not force it."],
            ["Eligibility is part of the domain",
             "π_DS is not defined on every retained episode. Treating every chat turn as eligible was a silent overclaim."],
            ["A_sel and A_task are different types",
             "Exact copied text can preserve a failed answer. Ablation evidence concerns A_sel. Complete service claims require A_task."],
            ["Deletion cost is a lift",
             "d_DS is a function of representatives. It cannot descend to Q_DS."],
            ["Ablation is a representation map",
             "Deleting a stored stage does not rerun the process that produced A."],
            ["Correction compliance is vertical",
             "Stage-obedience does not factor through π_DS. Score it before projection."],
            ["Presentation ≠ prediction",
             "A constructed counterexample shows current-answer equality does not give next-answer equality."],
            ["No namespace fusion",
             "Hidden Quotient, 39-screen, ℒ, R_n, and Q_DS remain distinct objects."],
        ],
        [150, 318],
        st,
    ))
    story.append(Spacer(1, 8))
    story.append(P(
        "Unchanged and not to be “improved” by this card: the 39-screen algebra, the Hidden Quotient "
        "kernel / localizability faces, toroidal cut-winding, OMNIBUS §10, and the residual-descent "
        "theorem on a declared domain.",
        st, "Note",
    ))

    story.append(P("1. The question", st, "H1"))
    story.append(P(
        "Which distinctions must a retained record preserve for the claim being made?",
        st,
    ))
    story.append(P(
        "That question is incomplete once a system both <i>computes</i> and <i>serves</i>. Split it.",
        st,
    ))
    story.append(P("1. <b>Audit / prediction.</b> Which distinctions must the retained record preserve for a declared witness W or a future output B?", st, "BulletBody"))
    story.append(P("2. <b>Service.</b> Which distinctions must the served interface preserve for this user object and this answer?", st, "BulletBody"))
    story.append(Spacer(1, 4))
    story.append(P(
        "The answers can differ. A stage can be internally necessary and visibly nonessential. "
        "A served answer can be identical while the next answer, under the same user input, is not.",
        st,
    ))

    story.append(P("2. Core geometry (carried forward)", st, "H1"))
    story.append(P(
        "Declare a source domain D, a retained map π : D → Q, and a witness W : D → Y. "
        "Work on attained labels Q = π(D).",
        st,
    ))
    story.append(P("<b>Witness-relative equivalence</b>", st, "H2"))
    story.append(P("x ∼_W y  ⇔  W(x) = W(y),      Q_W  ≅  im W.", st, "Eq"))
    story.append(P("<b>Non-descent locus</b>", st, "H2"))
    story.append(P("N_W(π)  =  { q ∈ Q  :  some x, y ∈ π⁻¹(q) have W(x) ≠ W(y) }.", st, "Eq"))
    story.append(P(
        "A point of N_W(π) is a same-label pair that still splits under W. "
        "The coarsest exact refinement retaining both the label and the witness is the image of (π, W), "
        "with its projection back to Q.",
        st,
    ))
    story.append(P("<b>Exact descent of a witness through π</b>", st, "H2"))
    story.append(P("W  =  W̄ ∘ π    ⇔    Eq(π)  ⊆  Eq(W).", st, "Eq"))
    story.append(P(
        "<b>Predictive closure</b> (deterministic). For a forward-invariant domain and update U : D → D, "
        "π(x) = π(y) implies π(Ux) = π(Uy). For a stochastic kernel, require equal next-observation laws "
        "on every measurable target whenever labels agree. A fitted one-trace table does not establish "
        "the universal condition.",
        st,
    ))
    story.append(P(
        "<b>No-shape.</b> Without extra hypotheses, any subset of Q can occur as N_W(π). "
        "A local collision does not determine global geometry. Openness, holonomy, and transport need "
        "their stated topological or smooth assumptions. Those assumptions are not supplied by the service layer.",
        st,
    ))

    story.append(P("3. The service stack", st, "H1"))
    story.append(P("X  —r→  E  —σ→  V  —q_DS→  Q_DS", st, "Eq"))
    story.append(make_table(
        ["Arrow", "Name", "Job"],
        [
            ["r", "retention", "Store execution as a typed episode record"],
            ["σ", "rendering", "Declare what the interface presents"],
            ["q_DS", "service quotient", "Identify episodes that serve the same object and answer"],
        ],
        [70, 120, 278],
        st,
    ))
    story.append(Spacer(1, 8))
    story.append(P(
        "X is execution. Access to a specimen E ∈ ℰ does not imply access to X. "
        "A stored stage label does not, by itself, prove the stage was displayed. "
        "Visibility is a separately retained observation Vis.",
        st,
    ))

    story.append(P("3.1 Eligible episodes", st, "H2"))
    story.append(P(
        "π_DS is defined only on an <b>eligible user-anchored response episode</b>: there is a governing request, "
        "a served user object O, and an answer-selection rule. If eligibility is UNKNOWN, the service projection "
        "is UNRESOLVED, not defaulted to “whatever the last assistant node said.”",
        st,
    ))

    story.append(P("3.2 Coordinate presentation", st, "H2"))
    story.append(P("E = (O, I, A),      π_DS(E) = (O, A).", st, "Eq"))
    story.append(P(
        "A_i deletes one identified separate stage record and leaves every other retained field untouched. "
        "O is the served user object, its anchor, and governing request. I is an ordered collection of separately "
        "represented interposition records (THOUGHTS, REASONING_RECAP, HIDDEN_META, CHECKING, tool-status bookkeeping). "
        "A is the answer payload under an explicit selection rule.",
        st,
    ))
    story.append(P(
        "Source node identities, order, role, tool dependencies, provenance, and visibility stay attached "
        "to the underlying retained record. They are not reconstructed from the pair (O, A).",
        st,
    ))

    story.append(P("3.3 Two answer types", st, "H2"))
    story.append(make_table(
        ["Symbol", "Meaning", "What evidence may use it for"],
        [
            ["A_sel", "selected recorded text used by the ablation files", "Exact string preservation"],
            ["A_task", "validated answer unit covering every span the governing request requires", "Complete substantive service"],
        ],
        [70, 210, 188],
        st,
    ))
    story.append(Spacer(1, 8))
    story.append(P(
        "E1–E4 establish claims about A_sel. Write A = A_task only when claiming complete substantive "
        "direct service. A last-node label is not a completion proof. A pause, availability statement, "
        "or first non-status node is not an answer unit.",
        st,
    ))

    story.append(P("3.4 Service equivalence", st, "H2"))
    story.append(P("E₁ ∼_DS E₂    ⇔    O(E₁) = O(E₂)  and  A(E₁) = A(E₂).", st, "Eq"))
    story.append(P(
        "This is an equivalence relation. Its quotient is canonically identified with im π_DS. "
        "Route-shape resemblance does not put different objects or different answers in one class.",
        st,
    ))

    story.append(P("4. The five service lemmas", st, "H1"))
    story.append(P(
        "These are the five additions the 9 September note proposed. They are stated here with domains.",
        st,
    ))

    story.append(P("Lemma S1 — Service factorization", st, "H2"))
    story.append(P(
        "On an eligible domain, there exists q_DS with π_DS = q_DS ∘ σ if and only if Eq(σ) ⊆ Eq(π_DS).",
        st,
    ))
    story.append(P(
        "The rendered trace must preserve the object anchor and the selected answer. If a display omits "
        "the object, attach the anchor to the trace or the factorization fails for the object witness. "
        "If it truncates required answer content, the factorization fails for that content witness. "
        "The diagram is a typed contract, not a claim that every live interface already implements it.",
        st,
    ))

    story.append(P("Lemma S2 — Ablation is class-preserving", st, "H2"))
    story.append(P(
        "Let A_i delete one identified separate stage while preserving O and every other retained field. "
        "If A(A_i E) = A(E) and O(A_i E) = O(E), then π_DS(A_i E) = π_DS(E). The original and ablated "
        "records determine the same direct-service class.",
        st,
    ))
    story.append(P(
        "If i is displayed as a separate service object, i is <b>visibly nonessential</b> for that specimen "
        "and answer witness. If display status is unverified, the established label is only "
        "<b>nonessential in the retained presentation</b>.",
        st,
    ))
    story.append(P(
        "This does not say the stage was computationally idle, and it does not say rerunning the hidden "
        "process without that stage would produce the same A. Ablation acts on a representation.",
        st, "Note",
    ))

    story.append(P("Lemma S3 — Deletion operators commute on fixed identities", st, "H2"))
    story.append(P("A_i² = A_i,      A_i A_j = A_j A_i.", st, "Eq"))
    story.append(P(
        "Hypothesis: stage identities are fixed and disjoint, and answer extraction does not depend on "
        "which of those records still remain. If classification or selection changes after each deletion, "
        "combined invariance needs its own check. A family of single-stage results does not certify an "
        "adaptive deletion procedure.",
        st,
    ))

    story.append(P("Lemma S4 — Minimal representatives exist in finite admissible families", st, "H2"))
    story.append(P(
        "Let R_E be the set of admissible derived representatives of the same object and answer, with "
        "preserved provenance, task content, and necessary dependencies. Let c_I(E′) = |I_vis(E′)| and "
        "let M_E be the argmin of c_I on R_E inside the service class. If the allowed deletion family is "
        "finite and contains an admissible fully ablated representative, the minimum is attained and equals zero. "
        "The preferred served form is then O → A.",
        st,
    ))
    story.append(P(
        "That preference is the declared service objective. The quotient makes the objective precise. "
        "It does not impose the preference independently of the contract.",
        st,
    ))

    story.append(P("Lemma S5 — Deletion cost does not descend", st, "H2"))
    story.append(P(
        "Define d_DS(E) as the minimum number of allowed unit-cost visible-stage deletions needed to reach "
        "a zero-interposition representative, or UNREACHABLE if none is admissible. When every visible stage "
        "is removable, d_DS(E) = |I_vis(E)|.",
        st,
    ))
    story.append(P(
        "Suppose E ∼_DS E* with I_vis(E*) empty and I_vis(E) nonempty. Any class-invariant distance on Q_DS "
        "would give d([E], [E*]) = 0, while d_DS(E) ≠ 0. Therefore d_DS is a function of representatives, "
        "not a metric on Q_DS.",
        st,
    ))
    story.append(P(
        "A separate retained-record cost d_ret may count stored records without asserting UI visibility. "
        "Neither cost is elapsed time, compute saved, heat, or a causal distance between pipelines.",
        st,
    ))

    story.append(P("5. Direct-Service Ablation Principle", st, "H1"))
    story.append(P(
        "If deletion of a separately retained execution-stage coordinate preserves the served object and "
        "the declared answer witness exactly, the original and ablated records determine the same "
        "direct-service class. Where the ablated representation is admissible and renderable, that coordinate "
        "is unnecessary as a separate visible object for that specimen.",
        st,
    ))
    story.append(P(
        "Internal computational necessity is not determined. This is Lemma S2 plus the renderability "
        "side-condition. The empirical job is locating actual separately represented stages, binding them "
        "to source answers, and checking preservation for the supplied transformations. That job is evidence, not geometry.",
        st,
    ))

    story.append(P("6. Answer fidelity and the continuation exception", st, "H1"))
    story.append(P(
        "Stage removal and answer selection are different maps. A selected node can be source-text-exact "
        "and still be the wrong unit: a pause copied as the answer, a shorter later node that drops an image "
        "description, an adjudicative rider left inside A, or two adjacent assistant nodes treated as one completion.",
        st,
    ))
    story.append(P("For an assistant-only continuation O → A₁ → I → A₂, stage-only ablation yields O → A₁ → A₂. "
                   "Deleting A₂ is a second operation. It requires a completion witness C(O, A₁) = 1 against the "
                   "governing request, and whole-content preservation additionally requires", st))
    story.append(P("W_req(O,  A₁ ‖ A₂)  =  W_req(O, A₁).", st, "Eq"))
    story.append(P(
        "A prefix can complete a task while differing from the recorded whole. Completion is not verbatim "
        "invariance. If A₂ carries required new material, consolidate it into one answer unit or retain it. "
        "If completion is UNKNOWN, stage removal can proceed while continuation removal stays UNRESOLVED.",
        st,
    ))

    story.append(P("7. Correction binding is a vertical witness", st, "H1"))
    story.append(P(
        "Let C_s be an active correction prohibiting visible stage s, and let Elig_s(t+1) mark the next "
        "comparable response. Successful stage correction requires Elig_s(t+1) = 1 ⇒ s ∉ σ(E_{t+1}).",
        st,
    ))
    story.append(P(
        "The prohibited object is behavioral: an independently emitted Checking stage is not the same as "
        "quoting the word in an audit. An assistant’s claim that the stage was needed does not establish the exception.",
        st,
    ))
    story.append(P("<b>Theorem C — compliance does not descend through π_DS.</b>", st, "H2"))
    story.append(P(
        "Take the same object and answer under the same active prohibition, once with stage s and once without. "
        "Then π_DS agrees and the compliance witness differs. Hence stage compliance does not factor through π_DS. "
        "After the stage is erased, the served pair (O, A) cannot recover whether the historical response obeyed the correction.",
        st,
    ))
    story.append(P(
        "Score historical compliance <b>before</b> projection. Score a repaired route on a new eligible observed "
        "response. Offline deletion cannot convert an original recurrence into a historical pass.",
        st,
    ))
    story.append(P("Audit refinement (use this when the claim is compliance, provenance, or visibility, not merely service):", st))
    story.append(P("π_audit(E)  =  ( π_DS(E),  K(E),  Vis(E),  Prov(E) ).", st, "Eq"))
    story.append(P(
        "K retains the active correction, eligibility, answer-selection decision, and outcome. This is the image "
        "of (π_DS, K, Vis, Prov) — the ordinary coarsest exact refinement for those witnesses. Answer-content "
        "corrections need their own predicate on A. No-status success does not imply their success.",
        st,
    ))

    story.append(P("8. Presentation is not prediction", st, "H1"))
    story.append(P(
        "The service quotient asks whether a current answer can be presented without separate interposition. "
        "Predictive geometry asks whether a retained state determines its successor. These are different obligations.",
        st,
    ))
    story.append(P("<b>Theorem P — current service labels do not give predictive closure.</b>", st, "H2"))
    story.append(P(
        "There exist a deterministic response map U_u, under a fixed next input u, and eligible episodes E₁, E₂ "
        "such that π_DS(E₁) = π_DS(E₂) and π_DS(U_u E₁) ≠ π_DS(U_u E₂).",
        st,
    ))
    story.append(P(
        "<b>Construction.</b> Let both episodes serve the same (O, A) now. Attach a correction bit k ∈ {0,1} "
        "that is not part of (O, A). Define the next answer payload to equal k. The current service labels agree; "
        "the next service labels differ.",
        st,
    ))
    story.append(P(
        "This is a constructed obstruction, not a finding about a hidden runtime register. It is enough to forbid "
        "the inference “we served the same answer, therefore the service record is an autonomous state.”",
        st,
    ))
    story.append(P(
        "The architecture may therefore minimize displayed stages while retaining a richer record for future control. "
        "Finite-horizon loss δ_h and the coarsest autonomous refinement of a declared output B remain the right tools "
        "for that richer record. Zero visible interposition does not supersede the 39-screen coordinates θ, z, and ρ "
        "relative to their own future-output witnesses.",
        st,
    ))
    story.append(P(
        "If a service companion residual is wanted, type it separately as R⁺ = (δC, δD, δK, δV). "
        "R⁺ gains an autonomous law only if its own descent condition holds. Adding a clock repairs cross-time "
        "ambiguity. It does not repair a collision already present at one time.",
        st,
    ))

    story.append(P("9. Rooms that stay separate", st, "H1"))
    story.append(make_table(
        ["Object", "Room", "Do not identify with"],
        [
            ["Q_DS", "served object and answer", "predictive state, audit state, ℒ"],
            ["N_W(π)", "labels that still split under W", "a physical hole, a social wound, a platform"],
            ["ker M_f on L²(μ)", "locally null functions", "hidden chat stages"],
            ["μ_sf vs localizable completion", "visibility repair vs gluing repair", "each other"],
            ["39-screen (θ, z, ρ)", "exact phase observations", "toroidal sector q, service stages"],
            ["ℒ", "shared non-sovereign encounter field", "mediator R, site lattice Λ_qsite(g)"],
            ["R_n = (ΔC, ΔD, ΔK)", "typed return residual", "scalar coherence, polarity"],
            ["cut winding / modular flux", "declared lattice currents", "a served answer"],
        ],
        [150, 160, 158],
        st,
    ))
    story.append(Spacer(1, 8))
    story.append(P(
        "Hidden Quotient translation is a dictionary, never a proof transfer. Discarded coordinate ↔ locally null "
        "function. L² witness ↔ finite-mass tests. Restore a point evaluation ↔ enlarge the witness, do not change μ. "
        "Service omission and witness restoration are different choices of observation. Quotienting away a stage "
        "because A_sel survived is omission. Adding Vis or K because compliance did not descend is restoration.",
        st,
    ))

    story.append(P("10. Operator card", st, "H1"))
    story.append(P("<b>Retain</b> (audit / prediction / correction)", st, "H2"))
    for line in [
        "governing request and object anchor",
        "answer-selection rule and the spans it used",
        "completion decision, with UNKNOWN allowed",
        "stage identities, order, and actual visibility",
        "active corrections and eligibility window",
        "tool / result dependencies the task still needs",
        "provenance sufficient to replay the record",
        "any coordinate required by a declared future output B",
    ]:
        story.append(P("•  " + line, st, "BulletBody"))

    story.append(P("<b>Serve</b> (direct service)", st, "H2"))
    for line in [
        "the user object",
        "the validated answer unit",
        "nothing else that Lemma S2 has shown to be visibly nonessential for this specimen and witness",
    ]:
        story.append(P("•  " + line, st, "BulletBody"))

    story.append(P("<b>Refuse to infer</b>", st, "H2"))
    for line in [
        "displayed  ⇒  internally unused",
        "deleted from the view  ⇒  deleted from the process",
        "same current answer  ⇒  same next answer",
        "same route shape  ⇒  same service class",
        "gate closure  ⇒  residual closure",
        "cardinality  ⇒  geometry",
        "model agreement  ⇒  empirical event",
    ]:
        story.append(P("•  " + line, st, "BulletBody"))

    story.append(P("11. What the carried evidence may and may not do", st, "H1"))
    story.append(P(
        "The 9 September ablation packet reports source-linked exact preservation for 287 selected answers, "
        "74 chains with separate stages, 156 separate records, and 137 chain-by-stage-class ledger rows. "
        "Those figures license A_sel-level class preservation under the supplied deletions. They do not license "
        "A_task completeness (located selection failures remain), live service-route mutation, a ranking of systems "
        "from unequal route samples, a claim that B50 or 455 is an identified internal pipeline, or pooling with "
        "DROP_IT v4.2 or any other denominator.",
        st,
    ))
    story.append(P(
        "Correction-binding (129 nonrecurrences / 198 comparable visible opportunities) keeps its own denominator, "
        "exclusions, and clustered-opportunity scope. It is a compliance witness, not a service-quotient identity. "
        "No result in this card changes Q1/Q2/Q3 status, the toroidal accepted-event discrepancy, or the Hidden "
        "Quotient’s standing as packaged classical analysis.",
        st,
    ))

    story.append(P("12. Checksum for this successor", st, "H1"))
    checks = [
        "Were audit witness and service witness kept distinct?",
        "Was eligibility part of the domain of π_DS?",
        "Was A_sel forbidden to stand in for A_task without a completion rule?",
        "Did ablation claims stay inside representation, not execution?",
        "Was d_DS kept off Q_DS?",
        "Was correction scored on π_audit, not recovered from (O, A)?",
        "Was predictive closure of π_DS treated as false in general, by Theorem P?",
        "Were Hidden Quotient, 39-screen, ℒ, and Q_DS left unfused?",
        "Did every empirical figure keep its original denominator?",
        "Does the final sentence stay inside the claim boundary?",
    ]
    for i, c in enumerate(checks):
        story.append(P(f"{i}.  {c}", st, "BulletBody"))

    story.append(Spacer(1, 16))
    story.append(P("Final banner", st, "H1"))
    story.append(banner_box([
        "RETAIN WHAT THE WITNESS NEEDS.",
        "SERVE THE OBJECT AND THE ANSWER.",
        "DO NOT MAKE A QUOTIENT DO A WITNESS'S JOB.",
    ], st))
    story.append(Spacer(1, 10))
    story.append(P(
        "v2.1 is an append-only successor. It does not rewrite the 39-screen, the Hidden Quotient faces, "
        "toroidal winding, or OMNIBUS §10. It gives the service layer exact lemmas and stops them from eating "
        "the rest of the geometry.",
        st, "Note",
    ))
    story.append(P("CC0 — No rights reserved", st, "FooterNote"))

    doc = SimpleDocTemplate(
        OUT,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=46,
        bottomMargin=42,
        title="GEOMETRY — Working Master v2.1",
        author="Anonymous",
        subject="Service-absorbed successor to Geometry + GQG",
    )
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print("wrote", OUT)


if __name__ == "__main__":
    build()
