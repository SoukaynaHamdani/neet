"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
edge case: intervals = [] 
creat 2 lists one for starts and one for ends then sort them and use 2 pointers , 
while s1 < n:
process the min value if it is a start increment count +1  else decrement it  -1  append the values of count to a list counts and return max of this list 

"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts=[]
        ends=[]
        n= len(intervals)
        if not intervals: return 0
        count=0 
        counts=[]
        for i in range(n):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)
        starts.sort()
        ends.sort()
        s1=0 
        e2=0
        while s1 < n:
            if starts[s1]<ends[e2]:
                count+=1
                counts.append(count)
                s1+=1
            else: 
                count-=1
                counts.append(count)
                e2+=1

        return max(counts)

