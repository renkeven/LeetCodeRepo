

class Solution:
    def __init__(self):
        self.count = 0
    
    def countGoodSubstrings(self, s: str) -> int:
        """
        speed it up without storing the cache
        """
        str_len = len(s)
        
        def check_unique(inp):
            if len(inp) == len(set(inp)):
                self.count += 1
            return
            
        for i in range(str_len - 2):
            check_unique(s[i:i+3])
        
        return self.count
        