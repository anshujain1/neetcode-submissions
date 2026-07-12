class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left =[]
        elem = 1
        for i in range(len(nums)):
            if i == 0:
                left.append(1)  
            else:
                elem *= nums[i-1]
                left.append(elem)

        elem = 1
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                left [ len(nums)-1]= 1 *(left[len(nums)-1])
                elem = nums[len(nums)-1]
                
            else:
                left[i] *= elem
                elem *= nums[i]

        return left        
                

            
            
            
            

                
                
                
