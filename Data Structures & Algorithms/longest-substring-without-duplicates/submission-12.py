class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        pos = {}
        result = 0
        for i in range(len(s)):
            if s[i] not in pos:
                pos[s[i]] = i 
            else:
                left = max( left , pos[s[i]] + 1 )
                pos[s[i]] = i
        
            result = max ( result , i - left + 1 )
        return result 

