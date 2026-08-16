class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = len(nums) -1 
        
        for i in range(len(nums)- 2, -1 ,-1 ) :
            if i+nums[i] >= farthest:
                farthest = i

            
        return farthest == 0

