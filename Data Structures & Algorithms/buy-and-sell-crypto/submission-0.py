class Solution:
    def recurse(self, prices, buyPrice, i, maxProfit):
        if i < 0:
            return maxProfit
        if buyPrice == -1:
            trans = self.recurse(prices, prices[i], i-1, maxProfit)
        else:
            trans = self.recurse(prices, buyPrice, i-1, max(maxProfit, buyPrice - prices[i]))
        no_trans = self.recurse(prices, buyPrice, i-1, maxProfit)
        return max(trans, no_trans)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        return self.recurse(prices, -1, n-1, maxProfit)