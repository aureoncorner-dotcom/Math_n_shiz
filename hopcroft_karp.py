"""Hopcroft–Karp maximum bipartite matching and König vertex cover.

Unit-cost hitting set of bipartite edges only. Not a general τ_a solver
and not a geometry-engine routine.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass


NIL = -1


@dataclass(frozen=True)
class HKResult:
    matching_size: int
    pair_left: tuple[int, ...]
    pair_right: tuple[int, ...]
    cover_left: tuple[int, ...]
    cover_right: tuple[int, ...]


class HopcroftKarp:
    def __init__(self, n_left: int, n_right: int, edges: list[tuple[int, int]]):
        self.nU = n_left
        self.nV = n_right
        self.adj: list[list[int]] = [[] for _ in range(n_left)]
        seen = set()
        for u, v in edges:
            if not (0 <= u < n_left and 0 <= v < n_right):
                raise ValueError("edge out of range")
            if (u, v) in seen:
                continue
            seen.add((u, v))
            self.adj[u].append(v)
        self.pair_u = [NIL] * n_left
        self.pair_v = [NIL] * n_right
        self.dist = [0] * (n_left + 1)  # last slot = NIL

    def _bfs(self) -> bool:
        q: deque[int] = deque()
        for u in range(self.nU):
            if self.pair_u[u] == NIL:
                self.dist[u] = 0
                q.append(u)
            else:
                self.dist[u] = float("inf")
        self.dist[self.nU] = float("inf")  # NIL
        while q:
            u = q.popleft()
            if self.dist[u] < self.dist[self.nU]:
                for v in self.adj[u]:
                    u2 = self.pair_v[v]
                    idx = self.nU if u2 == NIL else u2
                    if self.dist[idx] == float("inf"):
                        self.dist[idx] = self.dist[u] + 1
                        if u2 != NIL:
                            q.append(u2)
        return self.dist[self.nU] != float("inf")

    def _dfs(self, u: int) -> bool:
        if u == NIL:
            return True
        for v in self.adj[u]:
            u2 = self.pair_v[v]
            idx = self.nU if u2 == NIL else u2
            if self.dist[idx] == self.dist[u] + 1 and self._dfs(u2):
                self.pair_v[v] = u
                self.pair_u[u] = v
                return True
        self.dist[u] = float("inf")
        return False

    def maximum_matching(self) -> int:
        matching = 0
        while self._bfs():
            for u in range(self.nU):
                if self.pair_u[u] == NIL and self._dfs(u):
                    matching += 1
        return matching

    def konig_cover(self) -> tuple[tuple[int, ...], tuple[int, ...]]:
        """Cover from the last residual BFS. Call after maximum_matching."""
        self._bfs()
        reachable_u = {u for u in range(self.nU) if self.dist[u] != float("inf")}
        cover_u = tuple(u for u in range(self.nU) if u not in reachable_u)
        cover_v = tuple(
            v
            for v in range(self.nV)
            if self.pair_v[v] != NIL and self.pair_v[v] in reachable_u
        )
        return cover_u, cover_v

    def solve(self) -> HKResult:
        size = self.maximum_matching()
        cu, cv = self.konig_cover()
        if len(cu) + len(cv) != size:
            raise RuntimeError("König identity failed")
        return HKResult(
            matching_size=size,
            pair_left=tuple(self.pair_u),
            pair_right=tuple(self.pair_v),
            cover_left=cu,
            cover_right=cv,
        )


def _check():
    # Path of length 3: U={0,1}, V={0,1}, edges 0-0,0-1,1-1. ν=2, cover size 2.
    r = HopcroftKarp(2, 2, [(0, 0), (0, 1), (1, 1)]).solve()
    assert r.matching_size == 2
    # Empty graph
    r0 = HopcroftKarp(3, 2, []).solve()
    assert r0.matching_size == 0
    assert r0.cover_left == () and r0.cover_right == ()
    # One edge
    r1 = HopcroftKarp(2, 2, [(1, 0)]).solve()
    assert r1.matching_size == 1
    assert len(r1.cover_left) + len(r1.cover_right) == 1
    # Complete 3x3 minus a matching obstruction: full K_{3,3}
    edges = [(i, j) for i in range(3) for j in range(3)]
    r2 = HopcroftKarp(3, 3, edges).solve()
    assert r2.matching_size == 3
    print(
        {
            "path3": r.matching_size,
            "empty": r0.matching_size,
            "one_edge": r1.matching_size,
            "k33": r2.matching_size,
            "k33_cover": (r2.cover_left, r2.cover_right),
            "status": "PASS",
        }
    )


if __name__ == "__main__":
    _check()
