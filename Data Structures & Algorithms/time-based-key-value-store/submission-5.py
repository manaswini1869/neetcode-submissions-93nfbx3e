class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        values = self.time_map[key]
        left = 0
        right = len(values) - 1
        ans = ""
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
         
        return ans