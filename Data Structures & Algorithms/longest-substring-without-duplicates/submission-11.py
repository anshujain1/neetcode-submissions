class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexes = {}
        left = 0
        result = 0 
        for i in range(len(s)):
            if s[i] not in indexes:
                indexes[s[i]] = i
            else:
                left = max( left , indexes[s[i]] + 1)
                indexes[s[i]] = i
            length = i  - left + 1 
            if length >= result:
                result = length

        return result