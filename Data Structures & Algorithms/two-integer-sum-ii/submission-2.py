class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n - 1
        while i < j:
            tot = numbers[i] + numbers[j]
            if tot > target:
                j -= 1
            elif tot < target:
                i += 1
            else: return [min(i, j) + 1, max(i, j) + 1]
