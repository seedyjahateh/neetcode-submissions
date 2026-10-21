class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0

        for num in nums:
            temp = 1
            j = 1
            while num + j in nums:
                temp += 1
                j += 1

            if temp > length:
                length = temp

        return length