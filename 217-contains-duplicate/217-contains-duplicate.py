class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        """
        cache = {}
        for i in nums:
            if i in cache:
                return True
            else:
                cache[i] = 0
        
        return False