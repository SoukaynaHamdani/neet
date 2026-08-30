class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for st in strs:
            res+= (str(len(st))+"#"+st)
        return res
    def decode(self, s: str) -> List[str]:
        lst=[]
        i=0
        while i <len(s):
            j=i    # not 0
            while s[j] != "#":
                j+=1
            length= int(s[i:j])  #j is excldued 
            lst.append(s[j+1:j+1+length])
            i=j+1+length
        return lst
