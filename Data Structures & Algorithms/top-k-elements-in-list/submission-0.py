class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ 
        IN : arr nums, k 
        out k most freq 

     """
        import heapq 
        num_count_map=defaultdict(int)
        for num in nums:
            num_count_map[num]+=1
       # 1. كنجبدو الرقم والتردد بجوج باستعمال .items() عوض .values()
        max_neg = [(-count, num) for num, count in num_count_map.items()]
        heapq.heapify(max_neg) 
        res=[]
        for _ in range(k):
            freq, num = heapq.heappop(max_neg) 
            res.append(num)
        return res
    


     
