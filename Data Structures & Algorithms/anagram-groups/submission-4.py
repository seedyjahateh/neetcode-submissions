class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = {"".join(sorted(g)):[] for g in set(strs)}
        
        for s in strs:
            grps["".join(sorted(s))].append(s)

        return list(grps.values())