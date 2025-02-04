from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for row in zip(*matrix):
            transpose.append(row)
        return transpose
            






matrix = [[1,2,3]
        , [4,5,6],
          [7,8,9]]
x = Solution().transpose(matrix)
print(x)