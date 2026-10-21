class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))
        print(s, t)
        return s == t