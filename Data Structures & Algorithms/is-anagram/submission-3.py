class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not s and not t:
            return True
        elif not s:
            return False

        elif not t:
            return False

        else:
            a = sorted(s)
            b = sorted(t)
        
            return a == b
        