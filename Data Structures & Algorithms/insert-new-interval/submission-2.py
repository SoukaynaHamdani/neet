class Solution: 
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        #o(n) time and space 
        res=[]
        for i in range(len(intervals)):

            #newInterval ends before the current interval starts (no overlap)
            if newInterval[1]< intervals[i][0]:
                res.append(newInterval)
                #Append all remaining intervals from index i and return immediately
                res+= intervals[i:]
                return res 


            #newInterval starts  after the current interval ends (no overlap
            if newInterval[0]> intervals[i][1]:
                res.append(intervals[i])


            # Overlapping intervals — merge them by taking the outer bounds 
            else:
                newInterval= [
                    min(newInterval[0],intervals[i][0]),  
                    max(newInterval[1], intervals[i][1])] 
        
        # Edge Case: newInterval belongs at the very end 
        res.append(newInterval)

        return res 
