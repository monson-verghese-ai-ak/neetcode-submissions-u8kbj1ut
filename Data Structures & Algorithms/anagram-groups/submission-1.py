class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        dic = {}
        for s in strs:
            freq = [0] * 26
            for i in s:
                freq[ord(i) - ord('a')] += 1
            if tuple(freq) not in dic:
                dic[tuple(freq)] = [s]
            else:
                dic[tuple(freq)].append(s)
                
        return [v for k,v in dic.items()]
            