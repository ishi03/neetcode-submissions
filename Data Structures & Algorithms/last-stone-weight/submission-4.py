class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = -1 * heapq.heappop(stones)
            stone2 = -1 * heapq.heappop(stones)
            diff = stone1 - stone2
            if diff == 0:
                continue
            diff = diff * -1
            heapq.heappush(stones, diff)
        if stones:
            return -1 * stones[0]
        return 0