class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in indexes:
                return [indexes[need],i]
            else:
                indexes[nums[i]] = i 
            