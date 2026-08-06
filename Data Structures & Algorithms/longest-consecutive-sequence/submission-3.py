class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0

        for num in nums:
            if num-1 not in nums:
                length = 1
                current = num
                while current+1 in nums:
                    length += 1
                    current = current+1

                if length > ans:
                    ans = length
            
        return ans