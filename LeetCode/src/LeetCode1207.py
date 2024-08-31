from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        seen = set()

        
        for number in arr:
            if number in hashmap:
                hashmap[number] +=1
            else:
                hashmap[number] =1

        for key in hashmap:
            value = hashmap[key]
            if value in seen:
                return False
            if value not in seen:
                seen.add(value)
        return True



x=Solution()
arr = [1,2]
print(x.uniqueOccurrences(arr))

