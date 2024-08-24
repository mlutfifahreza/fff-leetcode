class Solution:
    def search(self, A, target):
        lo, hi = 0, len(A) - 1
        
        # Find the index of the smallest value using binary search.
        while lo < hi:
            mid = (lo + hi) // 2
            if A[mid] > A[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        # lo == hi is the index of the smallest value and also the number of places rotated.
        rot = lo
        lo, hi = 0, len(A) - 1
        
        # The usual binary search accounting for rotation.
        while lo <= hi:
            mid = (lo + hi) // 2
            realmid = (mid + rot) % len(A)
            if A[realmid] == target:
                return realmid
            if A[realmid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return -1
