class MedianFinder:
#space Space: O(n) 
    def __init__(self):
        self.lista=[]
 
    def addNum(self, num: int) -> None: #o(1) time 
        self.lista.append(num)
         

    def findMedian(self) -> float:   #O(n *log n)  
        self.lista.sort()
        n = len(self.lista)
        
        if n % 2 == 0:
            mid = n // 2
            return (self.lista[mid] + self.lista[mid - 1]) / 2.0
        else:
            mid = n // 2
            return float(self.lista[mid])