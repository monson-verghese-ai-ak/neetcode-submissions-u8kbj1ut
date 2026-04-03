class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLn = 1
        n = len(s)
        for i in range(0, n-1):
            arr = [0 for _ in range(26)]
            arr[ord(s[i]) - ord('a')] = 1
            for j in range(i+1, n):
                if arr[ord(s[j]) - ord('a')] == 0:
                    maxLn = max(maxLn, j-i+1)
                    arr[ord(s[j]) - ord('a')] = 1
                else:
                    break
        return maxLn