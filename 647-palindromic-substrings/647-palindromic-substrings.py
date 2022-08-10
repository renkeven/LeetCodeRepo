class Solution:
    def countSubstrings(self, s: str) -> int:

        def check_palin(s_):
            """check palindrome"""
            for i in range(len(s_)//2):
                if s_[i] != s_[-1 - i]:
                    return False
            return True
        
        cache = set()
        palin_len = 0
        max_len = len(s)
        
        for i in range(max_len):
            for j in range(max_len - i):
                str_ = s[j:j+1+i]
                
                if str_ in cache:
                    palin_len += 1
                
                elif check_palin(str_) == True:
                    palin_len += 1
                    cache.add(str_)
                        
        return palin_len