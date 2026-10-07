class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def solve( curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                curr.append(nums[i])
                used[i] = True
                solve(curr)
                used[i] = False
                curr.pop()
            
        solve([])
        return res

