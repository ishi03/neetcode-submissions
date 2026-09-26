class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        maxHeap = []
        heapq.heapify(maxHeap)

        for key, v in count.items():
            heapq.heappush(maxHeap, (-1*v, key))
        res = []
        for _ in range(k):
            x = heapq.heappop(maxHeap)
            res.append(x[1])
        return res