"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:   
         
        if not intervals: return True
        intervals.sort(key=lambda i:i.end)
        n=len(intervals)
        last_end= intervals[0].end
        for i in range(1,n): 
            curr_start , curr_end= intervals[i].start , intervals[i].end
            if last_end> curr_start: 
                return  False 
            else: 
                last_end=curr_end 

        return True
