class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        binary search, split in half, look left look right.
        """
        l = 0
        r = len(nums)
        idx = l
        
        if len(nums) < 1: return -1
        if nums[idx] == target: return idx
        
        while (l+1 < r):
            idx = (l + r)//2
            if nums[idx] > target:
                r = idx     
            elif nums[idx] < target:
                l = idx
            else:
                return idx
                
        return -1