class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        ans = 0
        left = 0
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = i
                length = i - left + 1
                ans = length
            else:
                left = max ( left , freq[s[i]] + 1 )
                freq[s[i]] = i
                length = i - left + 1

                if length > ans:
                    ans = length

        return ans
