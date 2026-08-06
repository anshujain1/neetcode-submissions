class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
            
        heap = []

        for num, frq in freq.items():
            heapq.heappush(heap, ( frq , num))

            if len(heap) > k:
                heapq.heappop(heap)

        
        return [pair[1] for pair in heap]
