class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        final_ans = []
        for i in range(len(nums)):
            if nums[i] in dic:
                final_ans = [dic[nums[i]], i]
                return final_ans
            else:
                dic[target - nums[i]] = i