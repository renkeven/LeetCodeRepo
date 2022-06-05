class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_n = 1001
        max_n = 0
        
        for i in nums:
            if i < min_n:
                min_n = i
            if i > max_n:
                max_n = i
                
        # def gcd(a,b):
        #     d = 0
        #     for i in range(1, min(a,b) + 1):
        #         if(a % i == 0 and b % i == 0):
        #             d = i
        #     return d

        def gcd(a,b):
            if a%b == 0:
                return b
            else:
                return gcd(b,a%b)
        
        return gcd(min_n, max_n)