class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[0 for _ in range(3)] for _ in range(2)]
        dp[0][0] = 1
        # row is A
        # col is L
        MOD = 1_000_000_007

        for i in range(n):
            new_dp = [[0 for _ in range(3)] for _ in range(2)]

            # P -> (A,L) from (0..1, 0..2) -> (0..1, 0..2)
            for a in range(2):
                for l in range(3):
                    new_dp[a][0] = (new_dp[a][0] + dp[a][l]) % MOD

            # A -> (A,L) from (0, 0..2) -> (1, 0..2)
            for l in range(3):
                new_dp[1][0] = (new_dp[1][0] + dp[0][l]) % MOD

            # L -> (A,L) from (0..1, 0..1) -> (0..1, 1..2)
            for a in range(2):
                for l in range(1,3):
                    new_dp[a][l] = (new_dp[a][l] + dp[a][l-1]) % MOD
            dp = new_dp
        
        res = 0
        for a in range(2):
            for l in range(3):
                res = (res + dp[a][l]) % MOD
        
        return res