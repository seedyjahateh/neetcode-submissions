class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        group = defaultdict(list)

        for s in strs:
            group["".join(sorted(s))].append(s)

        return list(group.values())