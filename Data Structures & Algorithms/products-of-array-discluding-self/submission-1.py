class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i, j = 1, len(nums) - 2

        pre, pos = [1] * len(nums), [1] * len(nums)
        pre[0], pos[-1] = nums[0], nums[-1]

        while i < len(nums) and j >= 0:
            pre[i] = nums[i] * pre[i - 1]
            pos[j] = nums[j] * pos[j + 1]
            i += 1
            j -= 1


        ans = [pos[1]]
        for i in range(1, len(nums) - 1):
            ans.append(pre[i - 1] * pos[i + 1])
        ans.append(pre[len(nums) - 2])
        
        return ans