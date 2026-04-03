class Solution:
   
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 1
        for i in numSet:
            if (i-1) not in numSet:
                length = 1
                num = i
                while num+1 in numSet:
                    length += 1
                    num += 1
                ans = max(ans, length)
        return ans