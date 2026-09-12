#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, ListFlowable, ListItem, HRFlowable,
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuBold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSerif", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSerifBold", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"))

OUT = "/home/workdir/artifacts/GEOMETRY_Typed_Defects_v0.2.pdf"
INK = HexColor("#1a1a1a")
RULE = HexColor("#2c3e50")
MUTED = HexColor("#555555")
BOX = HexColor("#eef2f5")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverKicker", fontName="DejaVu", fontSize=9, textColor=MUTED, leading=12, spaceAfter=4))
styles.add(ParagraphStyle(name="CoverTitle", fontName="DejaVuSerifBold", fontSize=18, textColor=INK, leading=22, spaceAfter=6))
styles.add(ParagraphStyle(name="CoverSub", fontName="DejaVu", fontSize=10, textColor=MUTED, leading=14, spaceAfter=10))
styles.add(ParagraphStyle(name="H1", fontName="DejaVuSerifBold", fontSize=13, textColor=RULE, leading=16, spaceBefore=12, spaceAfter=6))
styles.add(ParagraphStyle(name="H2", fontName="DejaVuBold", fontSize=11, textColor=INK, leading=14, spaceBefore=8, spaceAfter=4))
styles.add(ParagraphStyle(name="Body", fontName="DejaVu", fontSize=9.5, textColor=INK, leading=13, alignment=TA_JUSTIFY, spaceAfter=6))
styles.add(ParagraphStyle(name="Note", fontName="DejaVu", fontSize=8.5, textColor=MUTED, leading=12, spaceAfter=6))
styles.add(ParagraphStyle(name="Cell", fontName="DejaVu", fontSize=8, textColor=INK, leading=11))
styles.add(ParagraphStyle(name="CellB", fontName="DejaVuBold", fontSize=8, textColor=INK, leading=11))
styles.add(ParagraphStyle(name="BoxP", fontName="DejaVuBold", fontSize=9.5, textColor=INK, leading=13, alignment=TA_CENTER))

def P(text, style="Body"):
    return Paragraph(text, styles[style])

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.4)
    canvas.line(0.7*inch, letter[1]-0.5*inch, letter[0]-0.7*inch, letter[1]-0.5*inch)
    canvas.setFont("DejaVu", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.7*inch, letter[1]-0.42*inch, "Geometry of Typed Defects  ·  v0.2")
    canvas.drawRightString(letter[0]-0.7*inch, letter[1]-0.42*inch, "11 Sep 2026")
    canvas.line(0.7*inch, 0.48*inch, letter[0]-0.7*inch, 0.48*inch)
    canvas.drawString(0.7*inch, 0.32*inch, "CC0  ·  formal increment  ·  source freezes unchanged")
    canvas.drawRightString(letter[0]-0.7*inch, 0.32*inch, str(doc.page))
    canvas.restoreState()

story = []
story.append(P("Working increment to New geometry §§13–15 and GEOMETRY + GQG Working Master", "CoverKicker"))
story.append(P("Geometry of Typed Defects", "CoverTitle"))
story.append(P("v0.2  ·  11 September 2026  ·  CC0 / Anonymous", "CoverSub"))
story.append(P(
    "The non-descent locus is one set. Defects are not one kind. This increment adds the "
    "locus calculus (product, coarsening, refinement, restriction, predictive identification) "
    "and five named defect kinds matching the present corpus. It does not assign a shape to "
    "N<sub>W</sub>(π). The no-shape lemma remains in force."
))
story.append(P(
    "<b>Unchanged:</b> chemistry freeze, Hidden Quotient v1.7, 39-screen algebra, "
    "toroidal all-orders theorem, L=3 PASS, empirical status labels."
, "Note"))

story.append(P("0. Standing objects", "H1"))
story.append(P(
    "Declared domain D, total map π:D→Q=π(D), witness W:D→Y. "
    "N<sub>W</sub>(π) is the set of attained labels whose fibers are heterogeneous for W. "
    "Sector space S<sub>W</sub>=im(π,W). Canonical refinement π<sub>W</sub>(x)=(π(x),W(x)). "
    "Fiber diameter δ<sub>W</sub> when Y is metric. Any subset of Q can occur as N<sub>W</sub>(π)."
))

story.append(P("1. Calculus of loci", "H1"))
story.append(P("1.1 Product of witnesses — Lemma D1", "H2"))
story.append(P(
    "For W=(W<sub>1</sub>,W<sub>2</sub>), N<sub>(W1,W2)</sub>(π) = N<sub>W1</sub>(π) ∪ N<sub>W2</sub>(π). "
    "Joint recovery fails on the union. Cleaning one witness does not clean the other."
))
story.append(P("1.2 Coarsening the witness — Lemma D2", "H2"))
story.append(P(
    "If W′=f∘W then N<sub>W′</sub>(π) ⊆ N<sub>W</sub>(π). A coarser question can descend after a finer "
    "question has failed. This is New geometry §5 (E<sub>opt</sub> vs (E<sub>g</sub>,E<sub>b</sub>)) and §15.1 "
    "(Semaev relation vs specified signed output)."
))
story.append(P("1.3 Refining the observation — Lemma D3", "H2"))
story.append(P(
    "If π=r∘π′ then r(N<sub>W</sub>(π′)) ⊆ N<sub>W</sub>(π), and no new coarse defect can appear: "
    "if q ∉ N<sub>W</sub>(π), no point of r<sup>−1</sup>(q) lies in N<sub>W</sub>(π′)."
))
story.append(P("1.4 Restricting the domain — Lemma D4", "H2"))
story.append(P(
    "N<sub>W|C</sub>(π|C) ⊆ N<sub>W</sub>(π) ∩ π(C). The inclusion can be strict. Descent on C is not descent on D. "
    "Record the restriction separately (New geometry §15.3)."
))
story.append(P("1.5 Predictive locus is a static locus — Lemma D5", "H2"))
story.append(P(
    "A deterministic U:D→D admits an autonomous retained update on Q iff N<sub>π∘U</sub>(π)=∅. "
    "Matching a coarser one-step output B is N<sub>B</sub>(π)=∅, which does not imply autonomy of π. "
    "Sophie Germain on n ↦ 2n+1 is D5: r(3)=r(5) while r(U(3))≠r(U(5)). It is not a new closure theorem."
))

story.append(P("2. Five defect kinds", "H1"))
story.append(P(
    "Each kind has a test, a legal repair, and an illegal repair. A new example must name its kind or declare a sixth."
))

rows = [
    [P("Kind", "CellB"), P("Test", "CellB"), P("Legal repair", "CellB"), P("Illegal repair", "CellB")],
    [P("I  Operation loss", "Cell"),
     P("W_rel descends, W_out does not, same D and π", "Cell"),
     P("Retain the coordinate that splits the out-fiber (sign / y)", "Cell"),
     P("Treat vanishing of W_rel as recovery of W_out", "Cell")],
    [P("II  Unit / character loss", "Cell"),
     P("π kills a unit that W (a log or character) sees", "Cell"),
     P("Add a character with declared rank, kernel, modulus, precision", "Cell"),
     P("Promote one separating coefficient to a global theorem; omit gcd(h,ℓ)=1", "Cell")],
    [P("III  Subgroup injectivity", "Cell"),
     P("ker φ ∩ C = {e} while ker φ ≠ {e}", "Cell"),
     P("Restrict the source to C and record D4", "Cell"),
     P("Infer injectivity on G, a speedup, or GHS/HCDLP", "Cell")],
    [P("IV  Discrete sector", "Cell"),
     P("A_W = 0 on components, component constants disagree", "Cell"),
     P("Retain a sheet label, or pass to S_W", "Cell"),
     P("Treat vanishing vertical differential as descent on disconnected fibers", "Cell")],
    [P("V  Representability gap", "Cell"),
     P("N_W(π)=∅ but a needed object lies outside im π", "Cell"),
     P("Name the missing object; enlarge observation or codomain", "Cell"),
     P("Call the gap N_W(π). Collision ≠ missing dual", "Cell")],
]
t = Table(rows, colWidths=[1.15*inch, 1.85*inch, 1.85*inch, 1.85*inch])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), HexColor("#d6dde4")),
    ("BACKGROUND", (0,1), (-1,-1), BOX),
    ("GRID", (0,0), (-1,-1), 0.3, HexColor("#99a3ad")),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 4),
    ("RIGHTPADDING", (0,0), (-1,-1), 4),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
]))
story.append(t)
story.append(Spacer(1, 8))
story.append(P(
    "Kind I instance: E(F<sub>13</sub>), P=(2,1), Q=(3,3), −Q=(3,10); π keeps x-coordinates; "
    "x(P+Q)=12 ≠ x(P−Q)=11. Kind II instance: 1 and 1+√2 generate the same ideal in Z[√2]; "
    "reduction √2↦3 into F<sub>7</sub> separates base-3 logs mod 3. Pair separation is not Leopoldt."
, "Note"))

story.append(P("3. Identification table", "H1"))
idrows = [
    [P("A", "CellB"), P("B", "CellB"), P("Identify?", "CellB")],
    [P("N_W(π)=∅", "Cell"), P("existence of reduced witness W̄", "Cell"), P("Yes — Thm 14.2", "Cell")],
    [P("N_{π∘U}(π)=∅", "Cell"), P("autonomous retained update", "Cell"), P("Yes — D5", "Cell")],
    [P("N_{f∘W}(π)=∅", "Cell"), P("N_W(π)=∅", "Cell"), P("No — D2 is only ⊆", "Cell")],
    [P("N on a restriction C", "Cell"), P("descent on D", "Cell"), P("No — D4", "Cell")],
    [P("q ∈ N_W(π)", "Cell"), P("q ∈ ∂N_{W,ε}(π)", "Cell"), P("No — §14.8", "Cell")],
    [P("source-space transition", "Cell"), P("quotient-space boundary", "Cell"), P("No — lithium pressure", "Cell")],
    [P("Kind I existential zero", "Cell"), P("Kind I specified output", "Cell"), P("No", "Cell")],
    [P("Kind II pair character", "Cell"), P("global Schirokauer sufficiency", "Cell"), P("No", "Cell")],
    [P("Kind V missing dual", "Cell"), P("fiber collision", "Cell"), P("No", "Cell")],
    [P("combining projects", "Cell"), P("transferring proof", "Cell"), P("No", "Cell")],
]
t2 = Table(idrows, colWidths=[2.2*inch, 2.5*inch, 2.0*inch])
t2.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), HexColor("#d6dde4")),
    ("GRID", (0,0), (-1,-1), 0.3, HexColor("#99a3ad")),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 4),
    ("RIGHTPADDING", (0,0), (-1,-1), 4),
    ("TOPPADDING", (0,0), (-1,-1), 3),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [white, BOX]),
]))
story.append(t2)

story.append(P("4. Sector space and the predictive stack", "H1"))
story.append(P(
    "Kinds I–IV are multiple points in an r-fiber of S<sub>W</sub>→Q. The kind is the extra coordinate "
    "that splits that fiber. Kind V is a graph of a function plus a missing object outside the image. "
    "Canonical refinement π<sub>W</sub> kills I–IV for this W by retaining W; it is not a mechanistic coordinate "
    "and not a runtime predictor."
))
story.append(P(
    "Declare in order: static W and N<sub>W</sub>; update or kernel; predictive witness π∘U or the next-observation "
    "law (D5); horizon-h diameter δ<sub>h</sub><sup>B</sup>; clock only if fixed-time descent holds and cross-time fails. "
    "Do not feed future B-values into the present predictor. 39-screen and TD-COS-FH-001 instantiate D5 on different "
    "(D,U,W). They are not special cases of each other."
))

story.append(P("5. Disposition", "H1"))
story.append(P("TYPED DEFECT CALCULUS: ESTABLISHED", "BoxP"))
story.append(P("GLOBAL NON-DESCENT SHAPE: STILL NOT MEASURED", "BoxP"))
story.append(P("SOURCE FREEZES: UNCHANGED", "BoxP"))
story.append(Spacer(1, 8))
story.append(P(
    "Point Working Master §1 here. Keep proofs in the companion markdown. Reuse the arithmetic packet only with "
    "New geometry §15.5 qualifications: probable primality, Semaev resultant factors, prime-degree Weil restriction "
    "still has a base field, unit-character rank/kernel/precision, and h<sup>−1</sup> requires gcd(h,ℓ)=1."
, "Note"))

doc = SimpleDocTemplate(
    OUT, pagesize=letter,
    leftMargin=0.7*inch, rightMargin=0.7*inch,
    topMargin=0.65*inch, bottomMargin=0.65*inch,
    title="Geometry of Typed Defects v0.2",
    author="Anonymous",
)
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
