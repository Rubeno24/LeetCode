from typing import List

#2 pointer appraoch for containter with the most water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #left and right are the pointers in the beggining and end of the list
        left=0
        right=len(height)-1
        #maxNumber is what we are going to return and it will have the biggest number
        maxNumber=0
        #while loops keeps going untill left pointer is greater then the right pointer then we stop
        while left<right:
            #if the left wall is smaller we use that one in the calculations
            if height[left]<height[right]:
                #we calcualte the are which is a simple length times heigth, heigth is the smaller wall
                #length is the distance between right and left
                maxNumber=max(maxNumber,height[left]*(right-left))
                #after updating our max number we move over the smaller pointer 
                left+=1
            else:
                #here left is bigger so we use the smaller wall which is height[right] to get the area
                maxNumber=max(maxNumber,height[right]*(right-left))
                #we then update our max number and move the smaller pointer in
                right-=1
        #we then return the biggest number
        return maxNumber
            

x=Solution()
height =[1,8,6,2,5,4,8,3,7]

print(x.maxArea(height))