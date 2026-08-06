class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        elem = 1

        for i in range(len(nums)):
            if i == 0:
                ans.append(elem)
            else:
                elem *= nums[i-1]
                ans.append(elem)

        elem = 1
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                ans[i] *= 1
                elem = nums[i]
            else:
                ans[i] *= elem
                elem *= nums[i]

        return ans

