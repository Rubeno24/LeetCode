from collections import defaultdict
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build the graph from prerequisites
        self.graph = defaultdict(list)
        for x, y in prerequisites:
            self.graph[x].append(y)
        
        # process each query
        result = []
        for x, y in queries:
            result.append(self.DFS(x, y, set()))  # use a fresh seen set for each query
        return result

    def DFS(self, source, target, seen):
        # base case: if the source is the target
        if source == target:
            return True
        
        # mark the current source as visited
        seen.add(source)
        
        # explore neighbors
        for neighbor in self.graph[source]:
            if neighbor not in seen:
                if self.DFS(neighbor, target, seen):  # propagate True if the target is found
                    return True
        
        return False


# example usage
numCourses = 2
prerequisites = []
queries = [[1, 0], [0, 1]]
x = Solution().checkIfPrerequisite(numCourses, prerequisites, queries)
print(x)  # output: [False, False]
