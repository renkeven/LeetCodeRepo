class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #quicksort this, for now, just take the middle element as pivot
        
#         def _quicksort(arr, left, right):
#             if left < right:
#                 #find pivot and organise in the left->right range
#                 pivot_idx = _swaps(arr, left, right)
#                 _quicksort(arr, left, pivot_idx - 1)
#                 _quicksort(arr, pivot_idx+1, right)                
                
        
#         def _swaps(arr, left, right):
#             #use the right element as pivot, the ith element precedes numbers that 
#             #are larger than the pivor
#             pivot = arr[right]
#             i = left - 1
#             for j in range(left, right):
#                 if arr[j] < pivot:
#                     i+=1
#                     arr[i], arr[j] = arr[j], arr[i]
#             #after the loop, the big numbers should be right and small left, so we just need 
#             #to swap the right with the i+1th index
#             #print(right, i+1)
#             arr[right], arr[i+1] = arr[i+1], arr[right]

#             return i+1
            
            
#         _quicksort(nums, 0, len(nums)-1)
        
#         return nums
        
        
        
        
        
        
        #Going to use mergesort, that is sort an array
        def _mergeSort(nums):
            """
            keep breaking down an array until you get singlets. merge singlets from bottom up
            """
            if(len(nums) == 1): return nums
            midpt = len(nums)//2
            array1 = nums[:midpt]
            array2 = nums[midpt:]
        
            array1 = _mergeSort(array1)
            array2 = _mergeSort(array2)
    
            return _merge(array1, array2)
    
        def _merge(arr1, arr2):
            """
            look at first elements, append lower of the two to a list, move index of lower
            up by one, compare again until all elements are exhausted
            """
            merged_arr = []
            i = 0
            j = 0            

            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    merged_arr.append(arr1[i])
                    i+=1
                else:
                    merged_arr.append(arr2[j])
                    j+=1
            
            while i < len(arr1):
                merged_arr.append(arr1[i])
                i+=1
                
            while j < len(arr2):
                merged_arr.append(arr2[j])
                j+=1
            
            return merged_arr
            
        return _mergeSort(nums)