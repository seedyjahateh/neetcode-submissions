class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            s_std = ''.join(sorted(s))
            groups[s_std] = groups.get(s_std, []) + [s]
        return groups.values()