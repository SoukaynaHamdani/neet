class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """adjacency list / Cycle Detection
        Create an adjacency list mapping courses to their prerequisites. Then create a visited set and perform a dfs on each courses prerequisites if in the set return false .
        
        Time and space O(N+ P)  n nbr crs , P nbr preq """

        #create the hasmap 
        course_preq=defaultdict(list) #adjacency list   
        for crs,preq in  prerequisites:   #O(P) time  we dont add the cours that dont have preq 
                course_preq[crs].append(preq)
        
        visitset=set() 
        def dfs(crs):  # O(N+ P) time 
            #base cases 
            if course_preq[crs]==[]:   
                return True 
             
            if crs in visitset:
                return False 
            visitset.add(crs)  # o(n)
            
            for preq in course_preq[crs]: 
                    if not dfs(preq) :return False 
                    visitset.add(preq)
            visitset.remove(crs)   #backtracking 
            course_preq[crs]=[]    #memoization 
            return True 
        for crs in range(numCourses):
            if not dfs(crs):return False 
        return True 

 