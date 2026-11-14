class RandomizedSet:
    #insert to both a hashmap(num->index) and a list 
    #delete:copy the last val into the index of the element you want to remove. pop the end of the list. update the position of the last element in thre map and delet the val from the hashmap too. 
    #return random.choice(self.lista)
    def __init__(self):
        self.hmap=defaultdict(int)
        self.lista=[]

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False 
         
        self.hmap[val]=len(self.lista) # the index of the val tu inset is the lngth of the liste before adding the element to it 
        self.lista.append(val) 
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.hmap: 
            idx=self.hmap[val]

            last_val=self.lista[-1] #len(self.lista)-1 or -1 
            self.lista[idx]= last_val

            self.hmap[last_val]= idx
            self.lista.pop()
            del self.hmap[val]
            return True 
        return  False

    def getRandom(self) -> int:
            return random.choice(self.lista)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()