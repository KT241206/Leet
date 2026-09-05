class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2
        subtracted_sum = m * (n // m) * (n // m + 1)
        return(total_sum - subtracted_sum)
