class TimeMap:

    def __init__(self):
        self.h_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.h_map:
            self.h_map[key].append((timestamp, value))
        else:
            self.h_map[key] = []
            self.h_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.h_map: return ""
        left = 0
        right=len(self.h_map[key])-1
        ans = ""
        while left <= right:
            mid = left+ (right-left) // 2

            if self.h_map[key][mid][0] <= timestamp:
                ans = self.h_map[key][mid][1]
                left = mid+1
            else:
                right = mid-1

        return ans
        
