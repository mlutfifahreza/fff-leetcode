class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = n  # Initialize with a value larger than any possible distance
        
        for i, word in enumerate(words):
            if word == target:
                # Calculate direct distance
                d = abs(i - startIndex)
                # Compare direct distance vs. wrapping around the circle
                # The shortest distance is min(d, n - d)
                min_dist = min(min_dist, d, n - d)
        
        return min_dist if min_dist != n else -1