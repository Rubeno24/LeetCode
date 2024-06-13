from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        count=0
        for x in range(len(students)):
                count += abs(students[x] - seats[x])
        return count



x=Solution()
seats = [3,1,5]
students = [2,7,4]

print(x.minMovesToSeat(seats,students))