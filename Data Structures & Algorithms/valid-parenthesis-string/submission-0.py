class Solution:
    def checkValidString(self, s: str) -> bool:
        brackets = []
        stars = []
        for i in range(len(s)):
            x = s[i]
            if x == "(":
                brackets.append(i)
            elif x == "*":
                stars.append(i)
            elif x == ")":
                if brackets:
                    brackets.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        # match remaining "(" with "*"
        while brackets and stars:
            if brackets[-1] < stars[-1]:
                brackets.pop()
                stars.pop()
            else:
                return False
        return len(brackets) == 0