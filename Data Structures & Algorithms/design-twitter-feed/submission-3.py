class Twitter:

    def __init__(self):
        self.following = {} # who follows whom
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetList = []
        if userId not in self.following:
            self.following[userId] = {userId}
        for x in self.following[userId]: # list of following
            tweetList += self.tweets.get(x, [])
        # tweetList as minHeap
        heapq.heapify(tweetList)
        res = []
        for _ in range(10):
            if tweetList:
                t = heapq.heappop(tweetList)
                res.append(t[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = {followerId}
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.following and followeeId in self.following[followerId]:
            # self.following[followerId].discard(followeeId)
            self.following[followerId].remove(followeeId)
