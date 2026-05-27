class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = {}
        self.followees = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append([self.timestamp,tweetId])
        else:
            self.tweets[userId] = [[self.timestamp,tweetId]]
        self.timestamp += 1   

    def getNewsFeed(self, userId: int) -> List[int]:
        
        userIds = [userId]
        if userId in self.followees:
            userIds.extend(self.followees[userId])
        

        tweets = []

        for  u in userIds:
            if u not in self.tweets:
                continue
            for t in self.tweets[u]:
                heapq.heappush(tweets,t)
                if len(tweets) > 10:
                    heapq.heappop(tweets)
                   
        res = []
        while tweets:
            res.append(heapq.heappop(tweets)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)

        
