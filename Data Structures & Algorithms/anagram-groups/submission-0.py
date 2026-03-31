class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        dic = {}
        for s in strs:
            arr_s = [i for i in s]
            arr_s.sort()
            if tuple(arr_s) not in dic:
                dic[tuple(arr_s)] = [s]
            else:
                dic[tuple(arr_s)].append(s)
        
        return [v for k,v in dic.items()]