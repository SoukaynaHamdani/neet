import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
 
        count_map = {}
        for num in nums:
                count_map[num] = count_map.get(num, 0) + 1
        min_heap = []
        
        for num, count in count_map.items(): 
                heapq.heappush(min_heap, (count, num)) 
                if len(min_heap) > k:
                    heapq.heappop(min_heap)
        
        return [num for count, num in min_heap]
