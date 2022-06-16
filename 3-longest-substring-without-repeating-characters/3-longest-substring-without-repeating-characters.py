class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        just guess how many total symbols there are:
        ~40 according to google
        
        so 52 from alphabet, 10 from numbers, 1 from space, and let's say 38 symbols
        """
        
        if len(s) == 0:
            return 0
        
        window_size = min(95, len(s))
        
        def check_unique(inp):
            if len(inp) == len(set(inp)):
                return True
            else:
                return False
        
        while window_size > 1:
            for i in range(len(s) + 1 - window_size):
                if check_unique(s[i:i + window_size]):
                    return window_size
                
            window_size -= 1
                
        return 1