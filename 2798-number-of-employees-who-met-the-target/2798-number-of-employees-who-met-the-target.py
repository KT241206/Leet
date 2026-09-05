class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        # Check each employee one by one
        for hour in hours:
            # Employee met the target
            if hour >= target:
                count += 1
        return count