class TimeMap:

    def __init__(self):
        self.h_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.h_map:
            self.h_map[key][timestamp] = value
        else:
            self.h_map[key] = {}
            self.h_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.h_map: return ""
        values = list(self.h_map[key].keys())
        target = timestamp
        n = len(values)
        left = 0
        right=n-1
        ans = -1
        while left <= right:
            mid = left+ (right-left) // 2

            if values[mid] <= target:
                ans = values[mid]
                left = mid+1
            else:
                right = mid-1

        return self.h_map[key][ans] if ans != -1 else ""
        
