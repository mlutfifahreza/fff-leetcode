from typing import List
from heapq import heappush, heappop

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        # construct graph
        graph = {}  # point : [list[point, prob]]
        for i, edge in enumerate(edges):
            a, b = edge
            prob = succProb[i]
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append([b, prob])
            graph[b].append([a, prob])

        # priority queue
        min_heap = [(-1.0, start_node)] # (-prob, point)
        probabilities = {i: 0.0 for i in range(n)}
        probabilities[start_node] = 1.0

        while min_heap:
            current_prob, point = heappop(min_heap)
            current_prob = -current_prob

            if point == end_node:
                return current_prob

            for neighbor, edge_prob in graph.get(point, []):
                new_prob = current_prob * edge_prob
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heappush(min_heap, (-new_prob, neighbor))

        return 0.0
