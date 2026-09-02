class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        if m<n:
            m,n = n,m
        
        ans = 1
        j=1
        for i in range(m,m+n-1):
            ans *= i
            ans //= j
            j+=1
        return ans