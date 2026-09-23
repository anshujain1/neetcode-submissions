class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0 
        fast = 0 
        #finding the point where both pointers meet 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # going to the beginning of the cycle        
        slow2 = 0 
        while slow != slow2:
            slow = nums[slow] # first we use slow not slow2
            slow2 = nums[slow2]

        return slow 
