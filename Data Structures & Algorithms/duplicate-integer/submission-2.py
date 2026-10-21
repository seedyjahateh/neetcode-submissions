class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_freq = {n:0 for n in set(nums)}
        for num in nums:
            nums_freq[num] += 1
            if nums_freq[num] > 1:
                return True
        return False