class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for n in nums:
            count[n] = count.get(n, 0) + 1
        bucket = [[] for _ in range((len(nums)) + 1)]
        for key, v in count.items():
            bucket[v].append(key)

        res = []
        for i in range(len(bucket)-1, -1, -1):
            for x in bucket[i]:
                res.append(x)
            if len(res) == k:
                return res
        return []
        # maxHeap = [] # n log n; make maxHeap of bounded len.
        # heapq.heapify(maxHeap)

        # for key, v in count.items():
        #     heapq.heappush(maxHeap, (-1*v, key))
        # res = []
        # for _ in range(k):
        #     x = heapq.heappop(maxHeap)
        #     res.append(x[1])
        # return res