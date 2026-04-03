class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [[nums[0], nums[1]. nums[2]]]
        nums.sort()
        for i in range(1, len(nums)-2):
            to_sum = -nums[i]
            start = 0
            end = len(nums)-1
            while start < end:
                if start == i:
                    start += 1
                    continue
                if end == i:
                    end += 1
                    continue
                if nums[start] + nums[end] < to_sum:
                    start += 1
                elif nums[start] + nums[end] > to_sum:
                    end -= 1
                else:
                    triplets.append([nums[start], nums[i], nums[end]])
                    start += 1
        ansList = []
        for lis in triplets:
            lis.sort()
            if lis not in ansList:
                ansList.append(lis)
        return ansList
