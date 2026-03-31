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
        if zeros >= 2:
            return [0] * n
        if zeros == 1:
            return [mul if i == 0 else 0 for i in nums]    
        pref = [1]
        suf = [1]
        for i in range(1, n):
            pref.append(pref[-1] * nums[i-1])
     
        for i in range(n-2, -1, -1):
            suf.append(suf[-1] * nums[i+1])
        rev_suf = suf[::-1]
        print(pref, suf)
 
        print(pref, rev_suf)

        return [pref[i] * rev_suf[i] for i in range(n)]
