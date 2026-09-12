"""Dense Kuhn–Munkres (Hungarian) maximum-weight assignment.

Square weight matrix. Dummy-pad non-square inputs. Not a general
hitting-set solver and not a geometry-engine routine.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class KMResult:
    weight: float
    pair_left: tuple[int, ...]  # left u -> right v, or -1
    pair_right: tuple[int, ...]


def hungarian_max(weights: list[list[float]]) -> KMResult:
    n = len(weights)
    if any(len(row) != n for row in weights):
        raise ValueError("square matrix required")
    # duals
    y = [max(row) if row else 0.0 for row in weights]
    z = [0.0] * n
    pair_u = [-1] * n
    pair_v = [-1] * n

    def slack(u: int, v: int) -> float:
        return y[u] + z[v] - weights[u][v]

    for _ in range(n):
        # grow a Hungarian tree from all free left vertices
        parent_v = [-1] * n  # right v -> left u that reached it
        seen_u = [False] * n
        seen_v = [False] * n
        slack_v = [float("inf")] * n
        slack_from = [-1] * n
        queue = [u for u in range(n) if pair_u[u] == -1]
        for u in queue:
            seen_u[u] = True
        free_v = None
        while True:
            # scan labelled left vertices for smallest outgoing slack
            while queue:
                u = queue.pop()
                for v in range(n):
                    if seen_v[v]:
                        continue
                    s = slack(u, v)
                    if s < slack_v[v] - 1e-15:
                        slack_v[v] = s
                        slack_from[v] = u
                    if abs(s) <= 1e-12:
                        seen_v[v] = True
                        parent_v[v] = u
                        if pair_v[v] == -1:
                            free_v = v
                            queue = []
                            break
                        u2 = pair_v[v]
                        if not seen_u[u2]:
                            seen_u[u2] = True
                            queue.append(u2)
                if free_v is not None:
                    break
            if free_v is not None:
                break
            # dual update
            delta = min(slack_v[v] for v in range(n) if not seen_v[v])
            if delta == float("inf"):
                raise RuntimeError("infeasible assignment")
            for u in range(n):
                if seen_u[u]:
                    y[u] -= delta
            for v in range(n):
                if seen_v[v]:
                    z[v] += delta
                else:
                    slack_v[v] -= delta
            # add new equality edges
            for v in range(n):
                if not seen_v[v] and abs(slack_v[v]) <= 1e-12:
                    seen_v[v] = True
                    parent_v[v] = slack_from[v]
                    if pair_v[v] == -1:
                        free_v = v
                        break
                    u2 = pair_v[v]
                    if not seen_u[u2]:
                        seen_u[u2] = True
                        queue.append(u2)
            if free_v is not None:
                break
        # augment
        v = free_v
        while v is not None and v != -1:
            u = parent_v[v]
            prev = pair_u[u]
            pair_u[u] = v
            pair_v[v] = u
            v = prev

    weight = sum(weights[u][pair_u[u]] for u in range(n))
    return KMResult(weight=weight, pair_left=tuple(pair_u), pair_right=tuple(pair_v))


def _check():
    # identity: unique max
    r = hungarian_max([[1.0, 0.0], [0.0, 1.0]])
    assert r.weight == 2.0 and r.pair_left == (0, 1)
    # permutation
    w = [
        [1.0, 2.0, 0.0],
        [2.0, 3.0, 1.0],
        [0.5, 1.0, 4.0],
    ]
    r = hungarian_max(w)
    # brute
    import itertools
    best = max(
        sum(w[i][p[i]] for i in range(3))
        for p in itertools.permutations(range(3))
    )
    assert abs(r.weight - best) < 1e-9
    print({"weight": r.weight, "pair_left": r.pair_left, "brute": best, "status": "PASS"})


if __name__ == "__main__":
    _check()
