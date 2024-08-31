class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {}
        for i, edge in enumerate(edges):
            a,b = edge
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = -succProb[i]
            graph[b][a] = -succProb[i]
        
        print(graph)

        if start_node not in graph or end_node not in graph:
            return 0

        # greedy with heap
        heap = [[-1, start_node]]
        heapq.heapify(heap)

        visited = {}
        
        while heap:
            curr_succ, point = heapq.heappop(heap)
            # print("curr_succ, point", curr_succ, point)
            visited[point] = True
            # check if already reached end node
            if point == end_node:
                return -curr_succ
            # add curr point neighbors with lowest succ
            for neighbor, succ in graph[point].items():
                if neighbor not in visited:
                    heapq.heappush(heap, [-1 * abs(curr_succ) * abs(succ), neighbor])

        return 0