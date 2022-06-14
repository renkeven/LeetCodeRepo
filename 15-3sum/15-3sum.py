class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        # two pointer solution
        
        sol_arr = set()
        nums = sorted(nums)
        len_nums = len(nums)
        
        print(nums)
        
        for idx, i in enumerate(nums):
            if (idx > 1) and (nums[idx] == nums[idx - 1]): continue
            p1 = idx + 1
            p2 = len_nums - 1
            
            while p1 < p2 and p2 > 0 and p1 < len_nums:
                if p1 == idx:
                    p1 += 1
                    
                elif p2 == idx:
                    p2 -= 1
                
                elif nums[p1] + nums[p2] > -i:
                    p2 -= 1
                
                elif nums[p1] + nums[p2] < -i:
                    p1 += 1
                    
                else:
                    sol_arr.add(tuple(sorted([i, nums[p1], nums[p2]])))
                    p2 -= 1
                    p1 += 1
                    
        return [list(x) for x in sol_arr]
                    
            
            
        