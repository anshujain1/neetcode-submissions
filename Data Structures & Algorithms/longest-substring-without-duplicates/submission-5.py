class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        indexes= {}
        max_len= 0
        for i in range(len(s)):
            if s[i] not in indexes:
                indexes[s[i]] = i
            else:
                left = max(left, indexes[s[i]]+1)
                indexes[s[i]] = i
            length = i-left+1

            max_len= max(max_len , length)
        return max_len