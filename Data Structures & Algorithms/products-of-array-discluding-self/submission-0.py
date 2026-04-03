class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mul = 1
        for i in nums:
            if i != 0:
                mul *= i
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
        if zeros == 2:
            return [0] * n
        if zeros == 1:
            return [mul if i == 0 else 0 for i in nums]    
        
        return [mul // i for i in nums]