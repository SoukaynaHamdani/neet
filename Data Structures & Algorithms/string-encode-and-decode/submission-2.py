class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for st in strs:
            res+= (str(len(st))+"#"+st)
        return res
    def decode(self, s: str) -> List[str]:
        lst=[]
        for i in range(len(s)):
            if s[i]=="#":
                st=""
                for j in range(int(s[i-1])):
                    st+=s[i+1]
                    i+=1
                 
                lst.append(st)
        return lst 
