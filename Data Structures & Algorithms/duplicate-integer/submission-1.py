class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {n:0 for n in set(nums)}
        for n in nums:
            seen[n] += 1
            if seen[n] > 1:
                return True
        return False
        