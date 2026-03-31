class Solution:
    def recurse(self, prices, buyPrice, i, maxProfit, dp, state):
        if i < 0:
            return maxProfit
        if tuple([i, state]) in dp:
            return dp[tuple([i, state])]
        if buyPrice == -1:
            trans = self.recurse(prices, prices[i], i-1, maxProfit, dp, 1)
        else:
            trans = self.recurse(prices, buyPrice, i-1, max(maxProfit, buyPrice - prices[i]), dp, 2)
        no_trans = self.recurse(prices, buyPrice, i-1, maxProfit, dp, state)
        dp[i] = max(trans, no_trans)
        return dp[i]
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        state = 0
        dp = {}
        return self.recurse(prices, -1, n-1, maxProfit, dp, state)