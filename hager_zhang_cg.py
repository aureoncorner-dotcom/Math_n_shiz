"""Hager–Zhang CG-DESCENT (HZ 2005/2006), standalone.

Descent-truncated β, optional Powell restart, Armijo backtracking.
Synthetic tests only. Not a geometry engine routine.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import math

import numpy as np
from scipy.optimize import line_search as scipy_line_search


Vec = list[float]


def _dot(a: Vec, b: Vec) -> float:
    return sum(x * y for x, y in zip(a, b))


def _norm(a: Vec) -> float:
    return math.sqrt(_dot(a, a))


def _add(a: Vec, b: Vec, sb: float = 1.0) -> Vec:
    return [x + sb * y for x, y in zip(a, b)]


def _scale(a: Vec, s: float) -> Vec:
    return [s * x for x in a]


def _copy(a: Vec) -> Vec:
    return list(a)


@dataclass
class HZResult:
    x: Vec
    f: float
    gnorm: float
    iterations: int
    evaluations: int
    status: str


def hager_zhang_beta(
    delta: Vec,
    y: Vec,
    g: Vec,
    g_prev_norm: float,
    eta: float = 0.01,
) -> float:
    """Descent-truncated Hager–Zhang β.

    β^N = (y - 2 δ ||y||² / (δᵀy))ᵀ g / (δᵀy)
    β   = max(β^N, η_k),  η_k = -1 / (||δ|| min(η, ||g_{k-1}||))
    """
    dy = _dot(delta, y)
    if abs(dy) < 1e-16:
        return 0.0
    ynorm2 = _dot(y, y)
    # θ = y - 2 δ (||y||² / δᵀy)
    theta = _add(y, delta, -2.0 * ynorm2 / dy)
    beta_n = _dot(theta, g) / dy
    eta_k = -1.0 / (_norm(delta) * min(eta, max(g_prev_norm, 1e-16)))
    return max(beta_n, eta_k)


def line_search(
    f: Callable[[Vec], float],
    x: Vec,
    fx: float,
    g: Vec,
    delta: Vec,
    c1: float = 1e-4,
    max_eval: int = 40,
) -> tuple[float, Vec, float, int]:
    """Bounded golden-section search on [0, α_max] with Armijo accept.

    α_max is the first power-of-two that stops decreasing, capped.
    """
    gd = _dot(g, delta)
    if gd >= 0:
        delta = _scale(g, -1.0)
        gd = _dot(g, delta)

    evals = 0

    def phi(a: float) -> float:
        nonlocal evals
        evals += 1
        return f(_add(x, delta, a))

    # expand until increase or cap
    a_lo, f_lo = 0.0, fx
    a_hi = 1.0
    f_hi = phi(a_hi)
    while f_hi < f_lo and a_hi < 8.0 and evals < max_eval // 2:
        a_lo, f_lo = a_hi, f_hi
        a_hi *= 2.0
        f_hi = phi(a_hi)
    if f_hi < fx + c1 * a_hi * gd and evals < 4:
        return a_hi, _add(x, delta, a_hi), f_hi, evals

    # golden section on [0, a_hi]
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    lo, hi = 0.0, a_hi
    c = hi - gr * (hi - lo)
    d = lo + gr * (hi - lo)
    fc, fd = phi(c), phi(d)
    while hi - lo > 1e-8 and evals < max_eval:
        if fc < fd:
            hi, d, fd = d, c, fc
            c = hi - gr * (hi - lo)
            fc = phi(c)
        else:
            lo, c, fc = c, d, fd
            d = lo + gr * (hi - lo)
            fd = phi(d)
    alpha = 0.5 * (lo + hi)
    x_new = _add(x, delta, alpha)
    f_new = f(x_new)
    evals += 1
    if f_new > fx:
        # last-ditch Armijo from α=1
        alpha = 1.0
        for _ in range(20):
            x_new = _add(x, delta, alpha)
            f_new = f(x_new)
            evals += 1
            if f_new <= fx + c1 * alpha * gd:
                break
            alpha *= 0.5
    return alpha, x_new, f_new, evals


def cg_descent(
    f: Callable[[Vec], float],
    grad: Callable[[Vec], Vec],
    x0: Vec,
    *,
    tol: float = 1e-8,
    max_iter: int = 500,
    eta: float = 0.01,
    restart_c: float = 0.2,
) -> HZResult:
    x = _copy(x0)
    fx = f(x)
    g = grad(x)
    evals = 2
    delta = _scale(g, -1.0)
    g_prev = _copy(g)

    for k in range(max_iter):
        gnorm = _norm(g)
        if gnorm < tol:
            return HZResult(x, fx, gnorm, k, evals, "converged")

        def f_np(z):
            return f(list(z))

        def g_np(z):
            return np.asarray(grad(list(z)), dtype=float)

        ls = scipy_line_search(
            f_np, g_np, np.asarray(x, dtype=float), np.asarray(delta, dtype=float),
            gfk=np.asarray(g, dtype=float), old_fval=fx, c1=1e-4, c2=0.4,
        )
        alpha = ls[0]
        extra = ls[2] or 0
        extra_g = ls[3] or 0
        evals += extra + extra_g
        if alpha is None:
            delta = _scale(g, -1.0)
            ls = scipy_line_search(
                f_np, g_np, np.asarray(x, dtype=float), np.asarray(delta, dtype=float),
                gfk=np.asarray(g, dtype=float), old_fval=fx, c1=1e-4, c2=0.4,
            )
            alpha = ls[0]
            evals += (ls[2] or 0) + (ls[3] or 0)
            if alpha is None:
                alpha = 1e-4
        x = _add(x, delta, alpha)
        fx = f(x)
        g_new = grad(x)
        evals += 2

        y = _add(g_new, g_prev, -1.0)
        beta = hager_zhang_beta(delta, y, g_new, _norm(g_prev), eta=eta)
        # Powell restart only when the new direction would be almost aligned with +g
        if abs(_dot(g_new, g_prev)) > 0.9 * _dot(g_new, g_new):
            beta = 0.0

        delta = _add(_scale(g_new, -1.0), delta, beta)
        if _dot(g_new, delta) >= 0:
            delta = _scale(g_new, -1.0)

        g_prev = g
        g = g_new

    return HZResult(x, fx, _norm(g), max_iter, evals, "max_iter")


def rosenbrock(x: Vec) -> float:
    return sum(100.0 * (x[i + 1] - x[i] ** 2) ** 2 + (1.0 - x[i]) ** 2 for i in range(len(x) - 1))


def rosenbrock_grad(x: Vec) -> Vec:
    n = len(x)
    g = [0.0] * n
    for i in range(n - 1):
        g[i] += -400.0 * x[i] * (x[i + 1] - x[i] ** 2) - 2.0 * (1.0 - x[i])
        g[i + 1] += 200.0 * (x[i + 1] - x[i] ** 2)
    return g


def quadratic(x: Vec) -> float:
    # f = (x-1)² + 10(y+2)²
    return (x[0] - 1.0) ** 2 + 10.0 * (x[1] + 2.0) ** 2


def quadratic_grad(x: Vec) -> Vec:
    return [2.0 * (x[0] - 1.0), 20.0 * (x[1] + 2.0)]


if __name__ == "__main__":
    cases = {
        "rosenbrock": (rosenbrock, rosenbrock_grad, [-1.2, 1.0]),
        "quadratic": (quadratic, quadratic_grad, [4.0, 3.0]),
    }
    for name, (fn, gn, x0) in cases.items():
        result = cg_descent(fn, gn, x0, max_iter=200)
        print(
            name,
            {
                "status": result.status,
                "iterations": result.iterations,
                "evaluations": int(result.evaluations),
                "x": [round(float(v), 10) for v in result.x],
                "f": float(result.f),
                "gnorm": float(result.gnorm),
            },
        )
