from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        r = 1  # Start r at index 1
        l = 0
        
        while r < len(prices):
            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r+=1
            else:
                l = r  # Move l to r if prices[l] >= prices[r]
                r+=1
        
        return maxProfit


prices = [7,1,5,3,6,4]
x = Solution()
print(x.maxProfit(prices))
