class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        in : arr strings strs 
        out : list of sublist of anag
        order is not impo 

        anag : same char count 
        edge cases :
        """
        map ={}
        lst_sorted=[]
        for word in strs:
            new = ",".join(sorted(word))
            lst_sorted.append(new)


        for i in range(len(lst_sorted)):
            if lst_sorted[i] in map:
                map[lst_sorted[i]].append(strs[i])
            else: 
                map[lst_sorted[i]]=[strs[i]]
         
        return list(map.values())
         
       