import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.set = set() 
        self.current = 1  

    def popSmallest(self) -> int:
        if self.heap:
            smallest=  heapq.heappop(self.heap)
            self.set.add(smallest)
            return smallest
        else:
            smallest=self.current
            self.current +=1
            return smallest

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.set:
            heapq.heappush(self.heap,num)
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
num = 2
obj = SmallestInfiniteSet()
param_1 = obj.popSmallest()
obj.addBack(num)