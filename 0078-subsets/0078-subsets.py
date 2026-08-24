class Solution:
    def subsets(self, nums):
        result = []

        def solve(i, current):
            result.append(current[:])

            for j in range(i, len(nums)):
                current.append(nums[j])
                solve(j + 1, current)
                current.pop()

        solve(0, [])
        return result