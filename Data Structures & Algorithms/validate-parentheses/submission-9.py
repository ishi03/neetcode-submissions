class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        brackets = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        stack = []
        for x in s:
            if x in brackets.values():
                stack.append(x)
            else:
                if stack and stack.pop() == brackets[x]:
                    continue
                return False
        return True if not stack else False
    