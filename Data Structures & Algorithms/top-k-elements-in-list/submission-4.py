import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups={}
        for num in nums:
            groups[num]= 1+ groups.get(num,0)

        heap =[]
        for num , frq in groups.items():
            heapq.heappush(heap ,( frq , num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]
            
