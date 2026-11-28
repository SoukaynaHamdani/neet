class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
            
        """
        Two heaps: available tracks free room_ids, and used tracks (end_time, room_id) sorted by earliest finish.

Sort & Free: Sort meetings by start time, then pop all rooms from used with end_time <= start back into available.

Delay & Book: If available is empty, pop the earliest room from used and shift end = end_time + (end - start) before booking the smallest room_id and incrementing its count. 

time o(M logM + M logN ) M:nbr of meetings , N: nmbr of rooms """
       
        meetings.sort()
        avaible=[i for i in range(n)]  #0 1 2 3 ..  #miheap 
        used=[]   #(end_time , room_number)         #minheap 
        count=[0]*n    #count[n]= nmbr of meeting scheduled in room number n 

        for start, end in meetings:
            
            #finish meeting that finished at this start  time or before it  and move the used room to avaible 
            #used[0] gives the (end_time , room_number) that has the min end_time  
            while used and start>= used[0][0]:     #start>=end_time
                _ , room_number = heapq.heappop(used) 

                #add this room into the avaible heap cuz it is no more used 
                heapq.heappush(avaible, room_number)



            #scheduling 2 cases 
            #no room is avaible 
            if not avaible: 
                #pop min end from used rooms 
                end_time , room_number= heapq.heappop(used)
               
                #delay the meeting 
                #new end time of current meeeting after delay
                end = end_time+ ( end - start)
                #we add this room to avaible cuz it will be avaible at the new start time of the delay 
                heapq.heappush(avaible, room_number)


            # a room  is avaible 
            room_number=heapq.heappop(avaible)
            heapq.heappush(used, (end, room_number))
            count[room_number]+=1 
        return count.index(max(count))  #return first occurence  of max count 


