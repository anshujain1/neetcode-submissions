class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        pairs = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            a= nums[i]
            left=i+1
            right= len(nums)-1
            while left<right:
                curr = nums[left]+nums[right]
                if curr > -a:
                    right -=1
                elif curr < -a:
                    left +=1
                else:
                    pairs.append([a,nums[left],nums[right]])
                    left +=1
                    right -= 1

                    while left< right and  nums[left] == nums[left-1]:
                        left+=1
                    while left< right and nums[right] == nums[right+1]:
                        right -= 1
        return pairs
                    