class MyHashSet:

    def __init__(self):
        self.arr = []
        self.empty = True

    def add(self, key: int) -> None:
        if self.contains(key) == False:
            self.arr.append(key)
        else:
            pass

    def remove(self, key: int) -> None:
        if self.contains(key) == True:
            self.arr.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.arr
    
    def print(self):
        print(self.arr)



#Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(3)
obj.add(3)
obj.remove(3)
param_3 = obj.contains(4)
print(obj.contains(434))
obj.print()