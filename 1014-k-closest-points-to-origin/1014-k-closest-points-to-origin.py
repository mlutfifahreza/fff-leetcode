class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points

        def distance(p):
            return p[0]**2 + p[1]**2
        
        idx_distances = {}
        for i in range(len(points)):
            idx_distances[i] = distance(points[i])
        
        # sort by keys
        sorted_by_val = sorted(idx_distances.items(), key=lambda x:x[1])
        # print(f"sorted_by_val={sorted_by_val}")

        result = [0]*k
        counter = 0
        for idx, val in sorted_by_val:
            # print(idx, val)
            if counter == k:
                break
            
            result[counter] = points[idx]
            counter += 1
        
        return result