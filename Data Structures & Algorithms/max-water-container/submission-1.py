class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        ans = 0
        while l < r:
            currArea = (r-l) * min(heights[r], heights[l]) 
            ans = max(ans, currArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans