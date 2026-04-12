class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        else:
            values = self.time_map[key]
            n = len(values)
            l, r = 0, n-1
            res = ""
            while l <= r:
                mid = (l+r)//2
                if values[mid][0] <= timestamp:
                    res = values[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
        return res
                





