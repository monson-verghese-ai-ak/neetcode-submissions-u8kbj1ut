class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            seen[num] = False
        
        for num in nums:
            if seen[num] == True:
                return True
            else:
                seen[num] = True
        return False