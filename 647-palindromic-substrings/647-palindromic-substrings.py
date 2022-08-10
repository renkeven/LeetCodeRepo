class Solution:
    def countSubstrings(self, s: str) -> int:

        def check_palin(s_):
            """check palindrome"""
            for i in range(len(s_)//2):
                if s_[i] != s_[-1 - i]:
                    return False
            return True
        
        cache = set()
        palin_arr = []
        max_len = len(s)
        
        for i in range(max_len):
            for j in range(max_len - i):
                str_ = s[j:j+1+i]
                # if str_ in cache:
                #     continue
                # else:
                #     cache.add(str_)
                #     if check_palin(str_) == True:
                #         palin_arr.append(str_)
                
                if str_ in cache:
                    palin_arr.append(str_)
                
                elif check_palin(str_) == True:
                    palin_arr.append(str_)
                    cache.add(str_)
                    
    
        #print(palin_arr)
    
        return len(palin_arr)