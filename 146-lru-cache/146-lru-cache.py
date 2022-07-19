class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.pos_cache = dict()
        self.min_list = dict()
        
        self.counter = 0
        self.capacity = capacity
        self.full = False
        
    def get(self, key: int) -> int:
        if key in self.cache:
            """search pos_cache for key, pop min_list for old key, add 
            min_list with latest key, update pos_cache"""
            
            idx = self.pos_cache[key]
            self.min_list.pop(idx)
            
            self.pos_cache[key] = self.counter
            self.min_list[self.counter] = key
            self.counter += 1
            return self.cache[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            """update key, same as get"""
            self.cache[key] = value
            
            idx = self.pos_cache[key]
            self.min_list.pop(idx)
            
            self.pos_cache[key] = self.counter
            self.min_list[self.counter] = key
            self.counter += 1
            
        else:
            if (self.full) or (len(self.cache) == self.capacity):
                """
                set full for first time
                locate first element to go in dict (python dicts preserve order, this should
                be O(1)), locate key for first element
                
                pop this min_key from cache, add new key
                
                add position cache of new key
                place this position at back of queue
                """
                self.full = True
                
                min_idx = next(iter(self.min_list))
                min_key = self.min_list.pop(min_idx)
                
                self.cache.pop(min_key)
                self.cache[key] = value
                
                self.pos_cache[key] = self.counter
                self.min_list[self.counter] = key
                
                self.counter += 1
                
            else:
                self.cache[key] = value
                self.pos_cache[key] = self.counter
                self.min_list[self.counter] = key
                self.counter += 1
            
        pass
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)