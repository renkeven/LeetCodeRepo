hash_dict = {}

class Solution:
    def fib(self, n: int) -> int:
        
        if n < 2: return n
        
        if n in hash_dict:
            return hash_dict[n]
        
        else:
            hash_dict[n] = self.fib(n - 2) + self.fib(n - 1)
            
        return hash_dict[n]
        