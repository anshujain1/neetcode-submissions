class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        frq = {}
        ans = 0 
        left = 0 
        for i in range(len(s)):
            if s[i] not in frq:
                frq[s[i]] = i
            else:
                a = frq[s[i]]
                if a+1 > left:
                    left = a + 1 
                # updating to new substring elem index
                frq[s[i]] = i

            length = i - left + 1 
            if length > ans :
                ans = length
        return ans 

            
