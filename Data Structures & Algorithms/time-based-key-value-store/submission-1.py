class TimeMap:

    def __init__(self):
        self.mp = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append([value , timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        ans = ''
        if key not in self.mp:
            return ""
        arr = self.mp[key]
        left = 0
        right = len(arr)-1

        while left <=right:
            mid = left +(right-left)//2

            if arr[mid][1] <= timestamp:
                ans = arr[mid][0]
                left = mid+ 1
            else:
                right =mid-1

        return ans       
