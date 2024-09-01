class TimeMap:

    def __init__(self):
        self.ts = defaultdict(list) # key: []ts
        self.vals = defaultdict(list) # key: []val
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # print()
        self.ts[key].append(timestamp)
        self.vals[key].append(value)
        # print("set", self.ts[key])
        # print("set", self.vals[key])
        

    def get(self, key: str, timestamp: int) -> str:
        # print()
        # print(f"get key = {key} ts = {timestamp}")
        if key not in self.ts:
            return ""
        
        ts, vals = self.ts[key], self.vals[key]
        # print("get", ts)
        # print("get", vals)

        if timestamp < ts[0]:
            return ""
        
        if timestamp > ts[-1]:
            return vals[-1]
        
        l, r = 0, len(ts)-1
        while l <= r:
            i = (l+r) // 2
            if timestamp < ts[i]:
                r = i-1
            elif ts[i] < timestamp:
                l = i+1
            else:
                return vals[i]
        # print("l", l, "r", r, "timestamp", timestamp)
        return vals[r]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)