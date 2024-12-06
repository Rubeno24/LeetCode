from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashmap = {}
        count = 0
        #adds all the rows to a hashmap as a tuple a list (3,1,2,2)
        for row in grid:
                tupleRow = tuple(row)
                #checks if its in there is not its 1 as the key
                if tupleRow not in hashmap:
                    hashmap[tupleRow] = 1
                #already in there so we add 1 to the count
                else:
                    hashmap[tupleRow] +=1

        #tranpose matrix and get get a tuple list returned, so we get that first row of that 
        #tranpsoe matrix stored as row 
        for row in zip(*grid):
             #check if its the hashmap if so add the value of the hashmap to count
             if row in hashmap:
                  count += hashmap[row]
        return count




    
x = Solution()
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]


print(x.equalPairs(grid))


