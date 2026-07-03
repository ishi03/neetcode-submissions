class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        cards = {}
        for x in hand:
            cards[x] = cards.get(x, 0) + 1
        minHeap = list(cards.keys())
        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]
            for i in range(start, start + groupSize):
                if i not in cards:
                    return False
                cards[i] -= 1
                if cards[i] <= 0:
                    del cards[i]
                    # also delete it out of minHeap
                    if i != minHeap[0]:
                    # check that we delete the right thing
                    # if i is not at the top, it means i is not the smallest number
                    # a larger number was consumed before a smaller one
                        return False
                    heapq.heappop(minHeap)
        return True