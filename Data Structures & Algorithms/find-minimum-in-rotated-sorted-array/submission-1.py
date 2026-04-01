class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        res = nums[0]
        start = 0
        end = n-1

        while start <= end:
            if nums[start] < nums[end]:
                res = min(res, nums[start])
                break

            mid = (end + start) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1

        return res