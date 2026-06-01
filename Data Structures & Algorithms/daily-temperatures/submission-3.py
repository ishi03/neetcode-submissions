class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i in range(n-1,-1,-1):
            if not stack:
                stack.append((temperatures[i], i))
                continue
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return res
