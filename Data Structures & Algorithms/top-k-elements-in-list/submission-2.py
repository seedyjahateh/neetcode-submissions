class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[nums.count(n), n] for n in nums]
        counts.sort()
        topK = set()
        i = 0
        while len(topK) < k:
            topK.add(counts[::-1][i].pop(1))
            i += 1

        return list(topK)