class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for i in s:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i] += 1
        
        for i in t:
            if i not in dic2:
                dic2[i] = 1
            else:
                dic2[i] += 1
        
        for k, v in dic1.items():
            if k not in dic2:
                return False
            if dic2[k] != v:
                return False

        return True