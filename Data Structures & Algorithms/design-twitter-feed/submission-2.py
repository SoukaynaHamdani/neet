class Twitter:

    def __init__(self):
        self.followMap= defaultdict(set)
        self.tweetMap= defaultdict(list) #[count , tweetId] 
        self.count = 0  

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -=1 

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        res=[]
        minHeap=[]
        for followeeId in self.followMap[userId]:  #he is following me
            if followeeId in self.tweetMap:   #has posted 
                index=len(self.tweetMap[followeeId]) -1 # index of the latest tweet of this followee
                count , tweetId = self.tweetMap[followeeId][index]  ###     take the latest tweet  indx=5
                minHeap.append([count , tweetId , followeeId , index-1]) #  index of the tweeet before ourrs   indx=4
        heapq.heapify(minHeap) 
        
        while minHeap and len(res)<10:
            count, tweetId , followeeId,index = heapq.heappop(minHeap)  #4
            res.append(tweetId)
            
            if index>=0: #there is more old tweets of this user 
                count, tweetId=self.tweetMap[followeeId][index]           # the next tweeet cuz index is actuaindex-1   indx=4
                heapq.heappush(minHeap, [count , tweetId , followeeId , index-1])   #the second oldest indx=3

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
         self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:     #self 
            self.followMap[followerId].remove(followeeId)
