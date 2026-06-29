class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # q and maxHeap
        freq = Counter(tasks)
        maxHeap = [-x for x in freq.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        while maxHeap or q: # we have stuff to process
            time += 1
            if maxHeap:
                newCount = heapq.heappop(maxHeap) + 1
                # check if the new count is even valid before adding to q
                if newCount < 0:
                    q.append((newCount, time + n)) # new freq, next availablity
            if q:# time to consume
                # check if anything valid
                if q[0][1] == time:
                    x = q.popleft()
                    heapq.heappush(maxHeap, x[0])
        return time

