"""Pair-copula h-functions and a D-vine forward recursion.

h(u|v; θ) = ∂C(u,v;θ)/∂v = F_{U|V}(u|v).
Inverse h is included for a round-trip test.

Not a geometry-engine routine. Synthetic checks only.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable

from scipy.stats import norm


def _clip01(x: float, eps: float = 1e-12) -> float:
    return min(1.0 - eps, max(eps, x))


def h_independence(u: float, v: float, theta: float = 0.0) -> float:
    return _clip01(u)


def hinv_independence(p: float, v: float, theta: float = 0.0) -> float:
    return _clip01(p)


def h_gaussian(u: float, v: float, rho: float) -> float:
    if abs(rho) < 1e-15:
        return _clip01(u)
    if abs(rho) >= 1:
        raise ValueError("|rho| < 1 required")
    zu, zv = norm.ppf(_clip01(u)), norm.ppf(_clip01(v))
    z = (zu - rho * zv) / math.sqrt(1.0 - rho * rho)
    return float(norm.cdf(z))


def hinv_gaussian(p: float, v: float, rho: float) -> float:
    if abs(rho) < 1e-15:
        return _clip01(p)
    zp, zv = norm.ppf(_clip01(p)), norm.ppf(_clip01(v))
    z = zp * math.sqrt(1.0 - rho * rho) + rho * zv
    return float(norm.cdf(z))


def h_clayton(u: float, v: float, theta: float) -> float:
    """C(u,v)=(u^{-θ}+v^{-θ}-1)^{-1/θ}, θ>0."""
    if theta <= 0:
        return _clip01(u)
    u, v = _clip01(u), _clip01(v)
    inner = u ** (-theta) + v ** (-theta) - 1.0
    return _clip01((v ** (-theta - 1.0)) * inner ** (-1.0 - 1.0 / theta))


def hinv_clayton(p: float, v: float, theta: float) -> float:
    if theta <= 0:
        return _clip01(p)
    p, v = _clip01(p), _clip01(v)
    # invert h(u|v)=p for u
    # p = v^{-θ-1} (u^{-θ}+v^{-θ}-1)^{-1-1/θ}
    expo = -1.0 / (1.0 + 1.0 / theta)
    inner = (p / (v ** (-theta - 1.0))) ** expo
    u_neg_th = inner - v ** (-theta) + 1.0
    if u_neg_th <= 0:
        return 1.0 - 1e-12
    return _clip01(u_neg_th ** (-1.0 / theta))


H: dict[str, Callable[[float, float, float], float]] = {
    "indep": h_independence,
    "gauss": h_gaussian,
    "clayton": h_clayton,
}
HINV: dict[str, Callable[[float, float, float], float]] = {
    "indep": hinv_independence,
    "gauss": hinv_gaussian,
    "clayton": hinv_clayton,
}


@dataclass(frozen=True)
class PairEdge:
    family: str
    theta: float


def dvine_forward(u: list[float], edges: list[list[PairEdge]]) -> list[list[float]]:
    """D-vine forward h-transform.

    edges[k][i] is the pair-copula at tree k+1 between transformed
    variables that originated as (i, i+k+1).
    Returns the triangular array w[k][i] = u_{i|i+1,...,i+k}.
    w[0] is the raw uniforms.
    """
    d = len(u)
    w: list[list[float]] = [list(u)]
    for k in range(1, d):
        prev = w[k - 1]
        row = []
        if len(edges[k - 1]) != d - k:
            raise ValueError(f"tree {k} expected {d - k} edges")
        for i, edge in enumerate(edges[k - 1]):
            fn = H[edge.family]
            row.append(fn(prev[i], prev[i + 1], edge.theta))
        w.append(row)
    return w


def hinv(family: str, p: float, v: float, theta: float) -> float:
    return HINV[family](p, v, theta)


def hfun(family: str, u: float, v: float, theta: float) -> float:
    return H[family](u, v, theta)


def dvine_simulate(z: list[float], edges: list[list[PairEdge]]) -> list[float]:
    """Rosenblatt inverse on a D-vine (Aas et al. simulation).

    z are i.i.d. Uniform(0,1) innovations.
    edges[0][i] = C_{i+1,i+2}, edges[k][i] = C_{i+1,i+k+2 | i+2..i+k+1}.
    Returns u such that the D-vine Rosenblatt transform of u is z.
    """
    d = len(z)
    if len(edges) != d - 1:
        raise ValueError("need d-1 trees")
    V = [[0.0] * d for _ in range(d)]
    u = [0.0] * d
    u[0] = _clip01(z[0])
    V[0][0] = u[0]
    if d == 1:
        return u
    e = edges[0][0]
    u[1] = hinv(e.family, _clip01(z[1]), u[0], e.theta)
    V[1][0] = u[1]
    V[1][1] = hfun(e.family, u[1], u[0], e.theta)
    for i in range(2, d):
        cond = _clip01(z[i])
        # invert from highest tree down to tree 1
        for k in range(i - 1, 0, -1):
            e = edges[k][i - 1 - k]
            cond = hinv(e.family, cond, V[i - 1][k], e.theta)
        e = edges[0][i - 1]
        u[i] = hinv(e.family, cond, u[i - 1], e.theta)
        V[i][0] = u[i]
        V[i][1] = hfun(edges[0][i - 1].family, u[i], u[i - 1], edges[0][i - 1].theta)
        for j in range(1, i):
            e = edges[j][i - 1 - j]
            V[i][j + 1] = hfun(e.family, V[i][j], V[i - 1][j], e.theta)
    return u


def dvine_rosenblatt(u: list[float], edges: list[list[PairEdge]]) -> list[float]:
    """Forward Rosenblatt: z1=u1, z2=F(u2|u1), z3=F(u3|u1,u2), ... on a D-vine."""
    d = len(u)
    V = [[0.0] * d for _ in range(d)]
    z = [0.0] * d
    z[0] = _clip01(u[0])
    V[0][0] = z[0]
    if d == 1:
        return z
    e = edges[0][0]
    z[1] = hfun(e.family, _clip01(u[1]), u[0], e.theta)
    V[1][0] = _clip01(u[1])
    V[1][1] = z[1]
    for i in range(2, d):
        V[i][0] = _clip01(u[i])
        V[i][1] = hfun(edges[0][i - 1].family, V[i][0], V[i - 1][0], edges[0][i - 1].theta)
        for j in range(1, i):
            e = edges[j][i - 1 - j]
            V[i][j + 1] = hfun(e.family, V[i][j], V[i - 1][j], e.theta)
        z[i] = V[i][i]
    return z


def cvine_rosenblatt(u: list[float], edges: list[list[PairEdge]]) -> list[float]:
    """C-vine Rosenblatt, root order 1..d.

    edges[k][i] = copula of variable i+k+2 with root k+1 given 1..k.
    """
    cond = [_clip01(x) for x in u]
    z = [cond[0]]
    for k in range(len(u) - 1):
        root = cond[0]
        nxt = [hfun(e.family, cond[i + 1], root, e.theta) for i, e in enumerate(edges[k])]
        z.append(nxt[0])
        cond = nxt
    return z


def cvine_simulate(z: list[float], edges: list[list[PairEdge]]) -> list[float]:
    """Inverse C-vine Rosenblatt, root order 1..d."""
    d = len(z)
    u = [_clip01(z[0])] + [0.0] * (d - 1)
    given = [u[0]]
    for i in range(1, d):
        cond = _clip01(z[i])
        for t in range(i - 1, 0, -1):
            e = edges[t][i - 1 - t]
            cond = hinv(e.family, cond, given[t], e.theta)
        e = edges[0][i - 1]
        u[i] = hinv(e.family, cond, u[0], e.theta)
        given.append(_clip01(z[i]))
    return u


def inverse_rosenblatt(
    z: list[float],
    edges: list[list[PairEdge]],
    structure: str = "dvine",
) -> list[float]:
    """Inverse Rosenblatt: i.i.d. uniforms z -> copula-scale u."""
    if structure == "dvine":
        return dvine_simulate(z, edges)
    if structure == "cvine":
        return cvine_simulate(z, edges)
    raise ValueError("structure must be 'dvine' or 'cvine'")


def rosenblatt_transform(
    u: list[float],
    edges: list[list[PairEdge]],
    structure: str = "dvine",
) -> list[float]:
    if structure == "dvine":
        return dvine_rosenblatt(u, edges)
    if structure == "cvine":
        return cvine_rosenblatt(u, edges)
    raise ValueError("structure must be 'dvine' or 'cvine'")


def _check():
    # local inverse: hinv(h(u|v), v) ~ u
    errs = {}
    for fam, theta in [("indep", 0.0), ("gauss", 0.6), ("clayton", 2.0)]:
        worst = 0.0
        for u in (0.1, 0.3, 0.5, 0.7, 0.9):
            for v in (0.2, 0.5, 0.8):
                p = H[fam](u, v, theta)
                u2 = HINV[fam](p, v, theta)
                worst = max(worst, abs(u2 - u))
        errs[fam] = worst
        assert worst < 1e-8, (fam, worst)

    # 3-variable D-vine, independence: forward rows stay the raw u's
    u = [0.2, 0.5, 0.8]
    edges = [
        [PairEdge("indep", 0.0), PairEdge("indep", 0.0)],
        [PairEdge("indep", 0.0)],
    ]
    w = dvine_forward(u, edges)
    assert w[0] == u
    assert w[1] == [0.2, 0.5]
    assert w[2] == [0.2]

    # Gaussian D-vine triangle (old left|right convention)
    edges_g = [
        [PairEdge("gauss", 0.4), PairEdge("gauss", -0.3)],
        [PairEdge("gauss", 0.2)],
    ]
    wg = dvine_forward(u, edges_g)
    flat = [x for row in wg for x in row]
    assert all(0.0 < x < 1.0 for x in flat)

    # Rosenblatt inverse ∘ forward on a 4-var mixed D-vine
    edges4 = [
        [PairEdge("gauss", 0.4), PairEdge("clayton", 1.5), PairEdge("gauss", -0.2)],
        [PairEdge("gauss", 0.1), PairEdge("indep", 0.0)],
        [PairEdge("clayton", 0.8)],
    ]
    z = [0.15, 0.35, 0.55, 0.85]
    u_sim = dvine_simulate(z, edges4)
    z_back = dvine_rosenblatt(u_sim, edges4)
    inv_err = max(abs(a - b) for a, b in zip(z, z_back))
    assert inv_err < 1e-8, inv_err
    u = [0.2, 0.4, 0.6, 0.8]
    z_fwd = dvine_rosenblatt(u, edges4)
    u_back = dvine_simulate(z_fwd, edges4)
    fwd_err = max(abs(a - b) for a, b in zip(u, u_back))
    assert fwd_err < 1e-8, fwd_err

    # C-vine Rosenblatt round-trip, 3- and 4-var
    c3 = [
        [PairEdge("gauss", 0.5), PairEdge("clayton", 1.2)],
        [PairEdge("gauss", -0.2)],
    ]
    zc = [0.2, 0.4, 0.7]
    uc = cvine_simulate(zc, c3)
    zc2 = cvine_rosenblatt(uc, c3)
    c3_err = max(abs(a - b) for a, b in zip(zc, zc2))
    assert c3_err < 1e-8, c3_err
    c4 = [
        [PairEdge("gauss", 0.3), PairEdge("gauss", 0.1), PairEdge("clayton", 0.7)],
        [PairEdge("gauss", 0.2), PairEdge("indep", 0.0)],
        [PairEdge("clayton", 1.1)],
    ]
    z4 = [0.12, 0.33, 0.54, 0.76]
    u4 = cvine_simulate(z4, c4)
    z4b = cvine_rosenblatt(u4, c4)
    c4_err = max(abs(a - b) for a, b in zip(z4, z4b))
    assert c4_err < 1e-8, c4_err

    print(
        {
            "roundtrip_err": errs,
            "dvine_indep_ok": True,
            "rosenblatt_inv_err": inv_err,
            "rosenblatt_fwd_err": fwd_err,
            "cvine3_err": c3_err,
            "cvine4_err": c4_err,
            "status": "PASS",
        }
    )


if __name__ == "__main__":
    _check()
