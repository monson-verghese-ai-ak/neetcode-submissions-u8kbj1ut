class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for k,v in freq.items():
            bucket[v].append(k)
        # print(bucket)
        bucket = bucket[::-1]
        final_ans = []
        for lis in bucket:
            final_ans.extend(lis)
            
        return final_ans[:k-1]