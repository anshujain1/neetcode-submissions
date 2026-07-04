class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups={}
        for i in nums:
            if i in groups:
                groups[i] +=1
            else:
                groups[i]= 1
        
        a= list(sorted(groups.items(), key= lambda pair : pair[1]))[-k:]
        l=[]
        for pair in a:
            l.append(pair[0])

        return l
