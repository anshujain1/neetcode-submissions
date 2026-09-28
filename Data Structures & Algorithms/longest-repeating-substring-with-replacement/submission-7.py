class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        ans = 0 
        left = 0 
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1
            max_freq = max(max_freq , freq[s[i]])
            while i-left+1-max_freq > k:
                freq[s[left]] -=1
                left += 1
            
            a= i-left+1
            ans = max(ans ,a)
        return ans