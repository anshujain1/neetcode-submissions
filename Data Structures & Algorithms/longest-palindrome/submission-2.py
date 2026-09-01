class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = {}
        for i in range(len(s)):
            if s[i] in mp:
                mp[s[i]] += 1
            else:
                mp[s[i]] = 1

        ans = 0
        b=0
        for i,j in mp.items():
            if j%2 == 0:
                ans += j
            else:
                ans += j-1
                b = 1
            

        return ans+b