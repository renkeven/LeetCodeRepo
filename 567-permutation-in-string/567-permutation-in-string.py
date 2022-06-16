class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_cache = {}
        for i in s1:
            if i in s1_cache:
                s1_cache[i] += 1
            else:
                s1_cache[i] = 1
                
        s2_cache = {}
        for i in s2[:len(s1)]:
            if i in s2_cache:
                s2_cache[i] += 1
            else:
                s2_cache[i] = 1
        
        for idx, i in enumerate(s2[len(s1):]):
            if s1_cache == s2_cache:
                return True
            
            if i in s2_cache:
                s2_cache[i] += 1
            else:
                s2_cache[i] = 1
                
            if s2_cache[s2[idx]] == 1:
                del s2_cache[s2[idx]]
            else:
                s2_cache[s2[idx]] -= 1
        
        if s1_cache == s2_cache:
            return True
        
        else:
            return False
            