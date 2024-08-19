class Solution(object):
    def largestAltitude(self, gain):
        sum=0
        tallest=0
        for i in gain:
            sum += i
            if sum>tallest:
                tallest=sum
        return tallest

        # Input: gain = [-5,1,5,0,-7]
