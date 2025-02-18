from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen = set()
        for x in paths:
            seen.add(x[0])

        for x in paths:
            if x[1] not in seen:
                return x[1]


paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
x = Solution().destCity(paths)
print(x)