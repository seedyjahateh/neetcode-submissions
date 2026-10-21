class Solution:
    def isPalindrome(self, s: str) -> bool:
        chrs = ""

        for c in s:
            if c.isalnum():
                chrs += c.lower()

        n = len(chrs)
        if n == 1:
            return True
        
        i, j = 0, n - 1

        while i < j:
            if chrs[i] != chrs[j]:
                return False
            i += 1
            j -= 1

        return True
