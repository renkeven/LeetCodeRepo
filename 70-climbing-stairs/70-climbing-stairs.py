class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1,1,1,1,1,1
        1,2,1,1,1 = ncr(5,1)
        2,2,1,1 = ncr(4,2)
        2,2,2 = ncr(3,3)
        
        1,1,1
        1,2 = ncr(2,1)
        """
        
        cache = {}
        
        def factorial(k):
            if k < 2:
                return 1 
            if k in cache:
                return cache[k]
            else:
                cache[k] = k * factorial(k-1)
                return cache[k]
                
        def ncr(m, k):
            return factorial(m)/(factorial(m-k) * factorial(k))
            
        total_steps = 1
            
        for i in range(1, n//2 + 1):
            total_steps += ncr(n-i, i)
        
        return int(total_steps)