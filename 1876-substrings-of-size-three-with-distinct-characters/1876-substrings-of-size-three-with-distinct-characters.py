class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        hash_arr = {}
        str_len = len(s)
        
        def check_unique(inp):
            if inp in hash_arr:
                hash_arr[inp] += 1
            else:
                if len(inp) == len(set(inp)):
                    hash_arr[inp] = 1

            return
                    
            
        for i in range(str_len - 2):
            check_unique(s[i:i+3])
        
        return sum(hash_arr.values())
        