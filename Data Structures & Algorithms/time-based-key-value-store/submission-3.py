class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or not self.store[key]:
            return ""
        arr = self.store[key]
        lo, hi = 0, len(arr) - 1
        best = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid][0] <= timestamp:
                best = arr[mid][1]
                # try for a higher value
                lo = mid + 1
            else:
                hi = mid - 1
        return "" if best == -1 else best

