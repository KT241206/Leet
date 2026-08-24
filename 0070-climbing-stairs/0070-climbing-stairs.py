class Solution:
    def climbStairs(self, n):
        def solve(n, a, b):
            if n == 1:
                return a

            return solve(n - 1, b, a + b)

        return solve(n, 1, 2)