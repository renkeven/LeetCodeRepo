class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        binary search, split in half, look left look right.
        """
        l = 0
        r = len(nums) - 1
        idx = l
        
        # if len(nums) < 1: return -1
        # if nums[idx] == target: return idx
        
        while (l <= r):
            idx = (l + r)//2
            print(idx)
            if nums[idx] > target:
                r = idx - 1
            elif nums[idx] < target:
                l = idx + 1
            else:
                return idx
                
        return -1