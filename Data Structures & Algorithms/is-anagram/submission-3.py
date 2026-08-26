class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        counts= {}
        
        for char in s:
            counts[char]=1+ counts.get(char,0)
        for char in t:
            counts[char]=counts.get(char,0) -1

        return all(count==0 for count in counts.values())
    
