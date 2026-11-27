"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
edge case: intervals = [] 
creat 2 lists one for starts and one for end sort them 
use 2 pointers, 
while s1 < n:
process the min value if it is a start increment count +1  else decrement it  -1 keep track of max res  res=max(res,count)
return res  

#time o(n log n)
#space o(n)

"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
         
        n= len(intervals)
        if not intervals: return 0

        count=0 
        res=0  
        starts=sorted(i.start for i in intervals)
        ends=sorted(i.end for i in intervals)
     
        s1=0 
        e2=0
        while s1 < n:
            if starts[s1]<ends[e2]:
                count+=1
                s1+=1
            else: 
                count-=1
                e2+=1
            res=max(res,count)
        return res

