import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #set the left pointer to 1 since dividing by 0 is not worth doing
        left=1
        #set the right pointer to the max number in the piles array since thats the max ammount of bannas we can eat per hour
        right=max(piles)

        #we set the the result or the number of bannas the monkey can eat per hour to the max number since we know that will
        #work but we dont want the monkey to eat that fast so we can binary search to find the least number of bannas the 
        #monkey can eat per hour
        result=right

        #now we do a binary search
        while left<=right:
            middle = (left+right)//2
            
            hours=0

            #here we divide piles by the middle which represents hours and add it to hours
            for x in piles:
                hours+=math.ceil(x/middle)

            #the number of hours is less the target ammmount of hours so we cab bring in the rigth side
            if hours<=h:

                #we set result to middle since that answer works but it could be less
                result=middle
                #we can bring in the right variable since its less
                right=middle-1
            else:
                #hours>=h so we can bring in left pointer in
                left = middle+1
        #result is the number of bannas the monkey can eat per hour which is the least ammount to satisfy the condition
        #of the monkey eating not to many bannas to fast
        return result

            








piles = [3,6,7,11]
x=Solution()
print(x.minEatingSpeed(piles,8))