class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxPrice = 0
        minPrice = prices[0]

        for i in range(n):
            minPrice = min(minPrice, prices[i])
            maxPrice = max(maxPrice, prices[i] - minPrice)
        
        return maxPrice