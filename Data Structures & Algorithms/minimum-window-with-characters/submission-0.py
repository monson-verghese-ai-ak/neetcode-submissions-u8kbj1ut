class Solution:
    def check_dic_mt(self, dic):
        for k,v in dic.items():
            if v > 0:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        n = len(s)
        dic = {}
        for i in t:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        start = 0
        end = 0
        ans = s
        minL = len(s)
        while end < n:
            if s[end] in dic:
                dic[s[end]] -= 1
            while self.check_dic_mt(dic):
                if len(s[start:end+1]) < minL:
                    ans = s[start:end+1]
                    minL = len(s[start:end+1])
                if s[start] in dic:
                    dic[s[start]] += 1
                start += 1
            end += 1
            # print(s[start:end+1], ans, minL)
        
        return ans
