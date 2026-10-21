class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''

        ans = ''
        for i in range(len(strs)):
            ans += '0xC0' + strs[i] + '0xC1'
        return ans
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s) - 4:
            if s[i: i + 4] == '0xC0':
                i = i + 4
                word = ''
                while s[i: i + 4] != '0xC1':
                    word += s[i]
                    i += 1
                res.append(word)
                i = i + 4

        return res
