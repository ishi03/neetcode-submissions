class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [(timestamp, value)]
        else:
            self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        arr = self.hashmap[key]
        lo, hi = 0, len(arr) - 1
        best = -1
        # we have to look for timestamp
        # or for the greatest lesser value
        while lo <= hi:
            mid  = (lo + hi) // 2
            if arr[mid][0] <= timestamp:
                best = arr[mid][1]
                # try for higher value
            # if arr[mid][0] < timestamp:
                lo = mid + 1
            else:
                hi = mid - 1 
        return "" if best == -1 else best
