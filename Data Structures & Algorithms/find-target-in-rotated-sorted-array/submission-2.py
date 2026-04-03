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

        while start <= end:
            mid = (start + end) // 2
            print(start, mid, end)
            if nums[end] >= nums[start]:
                return self.normal_bs(nums, target, start, end)
            if nums[mid] == target:
                return mid
            
            elif nums[mid] <= nums[start]:
                end = mid - 1
            else:
                start = 1 + mid
        return -1