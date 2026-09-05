class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m = 1
        s = 0
        while n > 0:
            d = n % 10
            n = n // 10
            m *= d
            s += d

        return m - s