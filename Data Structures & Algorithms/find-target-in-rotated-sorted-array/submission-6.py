class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums)-1 
        while low <= high:
            mid = low + (high - low)//2
            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[high]:
                if nums[low] <= target <= nums[mid]:
                    high = mid 
                else:
                    low = mid + 1 
            
            else :
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1 
                else:
                    high = mid 

        return -1 

 