class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """binary search on column, then row"""
        u = 0
        d = len(matrix)
        r_idx = u
        
        l = 0
        r = len(matrix[0])
        c_idx = l
        
        while u+1 < d:
            r_idx = (u + d)//2
            print(r_idx)
            if matrix[r_idx][0] > target:
                d = r_idx
            elif matrix[r_idx][0] < target:
                u = r_idx
            else:
                return True
        
        if matrix[r_idx][0] > target:
            r_idx -= 1
            r_idx = max(0, r_idx)
            
        if matrix[r_idx][c_idx] == target: return True
        
        while l+1 < r:
            c_idx = (l + r)//2
            if matrix[r_idx][c_idx] > target:
                r = c_idx
            elif matrix[r_idx][c_idx] < target:
                l = c_idx
            else:
                return True
           
        print(r_idx, c_idx)
            
        return False