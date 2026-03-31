class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        final_ans = []
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        sorted_freq = list(sorted(freq.items(), key=lambda item:item[1]))[::-1]
        ln = len(sorted_freq)
        for i in range(k):
            final_ans.append(sorted_freq[i][0])
            if i+1 == ln:
                break
        return final_ans