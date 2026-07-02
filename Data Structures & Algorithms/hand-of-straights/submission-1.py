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
            start = minHeap[0] # first card we start hand with

            for i in range(start, start+groupSize):
                if i not in cards:
                    return False
                cards[i] -= 1
                if cards[i] <= 0: 
                # check that we are popping the right card
                    if i != minHeap[0]: # if a larger no finishes before smallest remaining
                    # grouping impossible
                        return False
                    heapq.heappop(minHeap)
        return True

        