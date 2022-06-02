class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        O(n) implies it passes through array once
        
        discussion soln says making a set is O(N), so why is iterating over a set 
        """
        #pick 1 and follow to the end, skipping those that have already been visited:
        
        nums = set(nums)
        
        longest = (1,-1,0) #impossible tuple such that the first element is always checked
        nums_len = len(nums)
        
        for idx, i in enumerate(nums):
            if longest[2] > nums_len // 2:
                return longest[2]
            
            if nums_len - idx < longest[2]:
                return longest[2]
            
            if i >= longest[0] and i <= longest[1]: continue
            
            current_len = 1
            pos = 1
            neg = 1
            while i+pos in nums:
                current_len += 1
                pos += 1
            while i-neg in nums:
                current_len += 1
                neg += 1
            
            if current_len > longest[2]:
                longest = (i - (neg - 1), i + (pos-1), current_len)
                
        return longest[2]