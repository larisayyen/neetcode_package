class TimeMap:

    def __init__(self):
        
        # set an empty dict 
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])


    def get(self, key: str, timestamp: int) -> str:
        
        # binary search to find the result

        res , values = "",self.store.get(key,[])

        l,r = 0,len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        
