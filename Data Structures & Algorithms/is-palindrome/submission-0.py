class Solution:
    def isAlpha(self, char):
        if char in r'[a-zA-Z0-9]':
            return True
        return False
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True