class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        
        numbers = []
        for i in nums:
            if i not in numbers:
                numbers.append(i)
        high = len(numbers)-1

        while low <= high:
            mid = low + (high - low)//2
            if target == numbers[mid]:
                return True

            if numbers[mid] >= numbers[high]:
                if numbers[low] <= target <= numbers[mid]:
                    high = mid 
                else:
                    low = mid + 1 
            
            else :
                if numbers[mid] <= target <= numbers[high]:
                    low = mid + 1 
                else:
                    high = mid 

        return False 

 