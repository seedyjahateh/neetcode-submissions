class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        num_freq = defaultdict(int)

        for num in nums:
            num_freq[num] += 1
        
        top_k = []
        for i in range(k):
            top_k.append(sorted(num_freq.items(), key=lambda item: item[1], reverse=True)[i][0])

        return top_k