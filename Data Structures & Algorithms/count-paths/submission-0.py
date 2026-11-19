class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """ base case : the last col and last row all filled wih ones 
        last row --> row = [1]*n 
        last coll gets filled automaticly when we do newRow=[1]*n 
        we start filling from the the bottom right corner and we keep filling to the left 

        so for each node we need to take the sum of our right and the position down us 

        o(n* m ) time
        o(n) space 
        """

        row=[1]*n 
        for i in range(m-2,-1,-1) :   #not m-1 cuz the row m-1 is handled by row=[1]*n    we can also do range(m-1) cuz  i is just a counter 
            new_row=[1]*n
            for j in range(n-2,-1,-1):
                new_row[j]=new_row[j+1] + row[j]
            row=new_row
        return row[0]
