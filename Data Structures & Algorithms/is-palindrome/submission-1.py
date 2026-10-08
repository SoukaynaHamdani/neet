class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        rigth=len(s)-1

        while left < rigth:

            while not s[left].isalnum():
                left+=1
            while not s[rigth].isalnum():
                rigth-=1
        
            if s[left].lower() != s[rigth].lower():
                return False
            else:
                left+=1
                rigth-=1
        return True 
        