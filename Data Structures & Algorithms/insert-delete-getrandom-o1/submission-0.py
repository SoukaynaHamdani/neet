class RandomizedSet:

    def __init__(self):
        self.hmap=defaultdict(int)
        self.lista=[]

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False 
        
        self.hmap[val]=len(self.lista)
        self.lista.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.hmap: 
            indextoremove=self.hmap[val]
            self.lista[indextoremove]=self.lista[len(self.lista)-1]
            self.hmap[self.lista[len(self.lista)-1]]=indextoremove
            self.lista.pop()
            del self.hmap[val]
        return val in self.hmap

    def getRandom(self) -> int:
            return random.choice(self.lista)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()