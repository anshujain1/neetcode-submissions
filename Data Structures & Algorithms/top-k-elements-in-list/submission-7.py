class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for num in nums:
            groups[num] = 1 + groups.get(num, 0)

        bucket = [[] for i in range(len(nums)+1)]

        for num, freq in groups.items():
            bucket[freq].append(num)
        ans =[]
        for i in range(len(bucket)-1, 0,-1):
            if len(ans)<k:
                for num in bucket[i]:
                    ans.append(num)
                if len(ans)==k:
                    return ans
            else:
                break
            
            