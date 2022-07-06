class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_encode = {'(':')', '{':'}', '[':']'}
        
        for c in s:
            if c in ['[', '(', '{']:
                stack.append(c)
            if c in [']', ')', '}']:
                if len(stack) == 0:
                    return False
                else:
                    if c != bracket_encode[stack.pop()]:
                        return False
                    
        if len(stack) > 0:
            return False
        
        return True