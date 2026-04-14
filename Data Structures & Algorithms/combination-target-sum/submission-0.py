class Solution:
    def recurse(self, nums, i, target, final_arr, arr):
        if i < 0 or target < 0:
            return
        if target == 0:
            if arr not in final_arr:
                final_arr.append(list(arr))
            return
        self.recurse(nums, i, target - nums[i], final_arr, arr + [nums[i]])
        self.recurse(nums, i-1, target - nums[i], final_arr, arr + [nums[i]])
        self.recurse(nums, i-1, target, final_arr, arr)
        return final_arr
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums) - 1
        final_arr = self.recurse(nums, n, target, [], [])
        # final_arr_uniques = list(set(final_arr))
        return final_arr