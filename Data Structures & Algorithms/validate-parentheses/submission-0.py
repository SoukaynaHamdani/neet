class Solution:
    def isValid(self, s: str) -> bool:
        mymap={"(":")", "{":"}","[":"]" }
        stack=[]
        for char in s:
            if char in mymap.keys():
                stack.append(char)
            else:   
                if stack  and mymap[stack[-1]]==char:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0





