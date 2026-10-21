class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {"".join(sorted(s)):[] for s in set(strs)}

        for s in strs:
            anagrams["".join(sorted(s))].append(s)
        return [val for val in anagrams.values()]
