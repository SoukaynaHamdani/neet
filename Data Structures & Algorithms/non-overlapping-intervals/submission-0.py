class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

         #nmbr of overlaping to remove  =  total -non overlaping count                

        #sort by end , take the first as non overlaping and its end as freetime , loop from 1 to n is start>= freetime mean the interval satrt after the end of last one we increment the count of non overlaping interv  and  update freetime to end  


        #time o(n log n )
        #Space o(n)
        intervals.sort(key=lambda i:i[1])
        freetime=intervals[0][1]
        non_ovelapping_count=1 
        n= len(intervals)

        for i in range(1,n):
            start , end =intervals[i]

            if start>= freetime: 
                non_ovelapping_count+=1     
                freetime = end 
                
        count=n-non_ovelapping_count         #nmbr of overlaping =  total -non overlaping count                
        return  count 