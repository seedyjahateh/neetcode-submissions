class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}
        counts = {')':0, '(':0, ']':0, '[':0, '}':0, '{':0}
        for c in s:
            counts[c] += 1
            if c in ['(', '[', '{']: # and not in stack
                stack.append(c)
            else:
                if stack and pairs[c] == stack[-1]:
                    stack.pop()
        return not stack and (counts['(']==counts[')'] and counts['[']==counts[']'] and counts['{']==counts['}'])
        
        