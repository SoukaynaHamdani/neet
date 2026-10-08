class Solution:
    def isValid(self, s: str) -> bool:
        mymap={")": "(", "}": "{", "]": "["}
        stack=[]
        for char in s:
            if char in mymap.keys():  #or just mymap
                if stack and mymap[char]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:   
                    stack.append(char)
            
        return len(stack) == 0





