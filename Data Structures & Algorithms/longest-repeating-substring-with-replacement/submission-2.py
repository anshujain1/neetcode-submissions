class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        ans = 0
        left = 0
        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
            max_freq = max( max_freq , freq[s[right]])
            while right -left - max_freq + 1  > k:
                freq[s[left]] -= 1
                left += 1
                
            a= right-left + 1 
            ans = max( ans , a)
        return ans
