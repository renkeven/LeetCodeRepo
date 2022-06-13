class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        len_s = len(s)
        
        
        if len_s%2 == 0:
            if s[:len_s//2] == s[len_s//2:][::-1]:
                return True
            else:
                return False
        
        else:
            if len_s == 1:
                return True
            elif s[:len_s//2] == s[len_s//2 + 1:][::-1]:
                return True
            else:
                return False
            
        return
        