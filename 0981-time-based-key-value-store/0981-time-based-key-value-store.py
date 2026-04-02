class TimeMap:

    def __init__(self):
        self.store = {}
        self.timestamp = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.store.get(key) is None:
            self.store[key]= [[timestamp],[value]]
        else:
            self.store[key][0].append(timestamp)
            self.store[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.store:
            return ""
        
        ts = self.store[key][0]
        l , r = 0, len(ts) - 1
        res = ""
        while l <= r:

            mid = (l + r) // 2

            if ts[mid] > timestamp:
                r = mid - 1
            else:
                res = self.store[key][1][mid]
                l = mid + 1 
        
        return res




        


