from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7

        n = len(edges) + 1

        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        max_depth = 0

        def dfs(node: int, parent: int, depth: int) -> None:
            nonlocal max_depth

            max_depth = max(max_depth, depth)

            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs(neighbor, node, depth + 1)

        # Root the tree at node 1
        dfs(1, 0, 0)

        # Number of valid assignments = 2^(max_depth - 1)
        return pow(2, max_depth - 1, MOD)