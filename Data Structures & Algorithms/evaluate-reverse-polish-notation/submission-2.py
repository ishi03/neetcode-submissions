class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for x in tokens:
            if x not in operations:
                stack.append(int(x))
            else:
                x1 = stack.pop()
                x2 = stack.pop()
                x3 = 0
                if x == "+":
                    x3 = x1 + x2
                if x == "-":
                    x3 = x2 - x1
                if x == "*":
                    x3 = x2 * x1
                if x == "/":
                    x3 = int(x2/x1)
                stack.append(x3)
        return stack.pop()