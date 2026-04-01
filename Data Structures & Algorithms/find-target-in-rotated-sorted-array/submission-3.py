class Solution:
    def normal_bs(self, nums, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)

        start = 0
        end = n-1
        res = nums[0]
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        pivot = start
        if self.normal_bs(nums, target, 0, pivot-1) != -1:
            return self.normal_bs(nums, target, 0, pivot-1) 
        return self.normal_bs(nums, target, pivot, n-1) 