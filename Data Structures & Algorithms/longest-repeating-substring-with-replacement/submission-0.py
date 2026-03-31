class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
      
        start = 0
        end = 0
        ans = 1
        freqs = [0 for _ in range(26)]
        maxFreq = 0
        while end < n:
            freqs[ord(s[end]) - ord("A")] += 1
            maxFreq = max(maxFreq, freqs[ord(s[end]) - ord("A")])
            while (end - start + 1) - maxFreq > k:
                freqs[ord(s[start]) - ord("A")] -= 1
                start += 1
            ans = max(ans, end - start + 1)
            end += 1
        return ans