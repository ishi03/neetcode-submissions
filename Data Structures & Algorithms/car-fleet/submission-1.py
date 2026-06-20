class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pt = []
        for i in range(n):
            pt.append((position[i], speed[i]))
        pt.sort(reverse=True)

        stack = []
        for i in range(n):
            time = (target - pt[i][0])/pt[i][1]
            if not stack:
                stack.append(time)
            if stack and stack[-1] < time:
                stack.append(time)
        return len(stack)