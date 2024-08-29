class Solution:
    def removeStones(self, points):
        uf = {}

        n = len(points)

        def find(k):
            # print(f"find({k})")
            if k not in uf:
                uf[k] = k

            if uf[k] != k:
                uf[k] = find(uf[k])
            
            return uf[k]
            
        for x,y in points:
            uf[find(x)] = find(~y)
        
        # print("uf", uf)
        
        coll_count = len({find(k) for k in uf})

        # print("coll_count", coll_count)
        # print("len(points)", len(points))

        return len(points) - coll_count