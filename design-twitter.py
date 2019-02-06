def cmp(x, y):
    return y[0] - x[0]

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = {}  # user id -> [tweet id]
        self.following = {} # user id -> user id -> dummy
        self.tick = 0
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        tick = self.tick
        self.tick += 1
        if userId in self.tweets:
            self.tweets[userId].append((tick, tweetId))
        else:
            self.tweets[userId] = [(tick,tweetId)]
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        following = [userId]
        if userId in self.following:
            following += self.following[userId].keys()
        tweets = []
        for u in following:
            if u in self.tweets:
                tweets += self.tweets[u][-10:]
        tweets = sorted(tweets,cmp=cmp)[:10]
        return [t[1] for t in tweets]
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        if followerId in self.following:
            self.following[followerId][followeeId] = True
        else:
            self.following[followerId] = {followeeId:True}

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.following:
            return
        if followeeId not in self.following[followerId]:
            return
        del(self.following[followerId][followeeId])
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
