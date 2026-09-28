class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = low + (high - low) // 2
            days_needed = 1
            curr_weight = 0
            for weight in weights:
                if curr_weight + weight > mid:
                    days_needed += 1
                    curr_weight = 0
                curr_weight += weight

            if days_needed <= days:
                high = mid
            else:
                low = mid + 1

        return low
