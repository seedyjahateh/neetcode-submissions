class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums) - 1):
            diff = target - nums[i]
            temp = nums[:i] + nums[i + 1:]
            if diff in temp:
                return [min(i, temp.index(diff) + 1), max(i, temp.index(diff) + 1)]

        