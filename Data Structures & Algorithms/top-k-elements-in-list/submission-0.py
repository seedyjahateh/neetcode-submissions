class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1

        ans = sorted(numFreq.items(), key=lambda x:x[1], reverse=True)[:k]

        return list(dict(ans).keys())
