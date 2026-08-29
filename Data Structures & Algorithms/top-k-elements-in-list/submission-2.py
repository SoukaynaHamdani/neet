class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count_map=defaultdict(int)
        for num in nums:
            num_count_map[num]+=1
        reversed_count_num =[[] for _ in range(len(nums) + 1)]
        for num , freq in  num_count_map.items():
               reversed_count_num[freq].append(num)
        res=[]
        for i in range(len(reversed_count_num)-1, 0 , -1):
            for num in reversed_count_num[i]:
                res.append(num)
                if len(res)==k:
                 return res

         

