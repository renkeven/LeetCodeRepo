class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #subtract_list = [i - target for i in nums]
        common_val = list(set(nums).intersection([target - i for i in nums]))
        
        if(target/2. in common_val and len(common_val) == 3):
            common_val.remove(target/2)
            
        if(len(common_val) == 1):
            return [i for i,val in enumerate(nums) if val==common_val[0]]
        else:    
            return [nums.index(common_val[0]), nums.index(common_val[1])]
        