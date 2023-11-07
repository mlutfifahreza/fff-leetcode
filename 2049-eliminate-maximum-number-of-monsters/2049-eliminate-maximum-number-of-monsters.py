class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        max_steps = []
        for i in range(len(dist)):
            max_steps.append(math.ceil(dist[i] / speed[i]))

        # print(max_steps)
        max_steps.sort()
        # print(max_steps)

        for i in range(len(max_steps)):
            if max_steps[i] <= i:
                return i
        
        return len(max_steps)