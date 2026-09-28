class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = low + (high - low) // 2
            subarrays = 1
            curr_sum = 0 

            for i in range(len(nums)):
                if curr_sum + nums[i] > mid:
                    subarrays += 1
                    curr_sum = 0 
                curr_sum += nums[i]
            
            if subarrays <= k:
                high = mid 
            else:
                low = mid + 1 
            
        return low