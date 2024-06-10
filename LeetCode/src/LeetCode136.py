from typing import List


"""
we can see what number only appears once using bit wise manipulation. This is done using the xor operator.
Lets say we have an array of the numbers 2,2,1
010 =2
010 =2
001 =1
the xor operator reuturns 0 when two numbers are the same and returns 1 when they are different
so when we add all numbers we get the binary number of just 1 
last column we get a 0 
middle we get a 0 since 1 and 1 are the same we get a zero
first column we get a 1 since 0 and 0 gives us 0 and 0 and 1 give us 1

Just remeber that xor all numbers get rid of the dupe
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for numbers in nums:
            result^=numbers
        return result


x= Solution()

list = [2,2,1]
print(x.singleNumber(list))
