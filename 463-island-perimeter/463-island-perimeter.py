class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def get_perimeter(arr, i, j):
            val = 4
            if arr[i+1][j] == 1:
                val-=1
            if arr[i-1][j] == 1:
                val-=1
            if arr[i][j-1] == 1:
                val-=1
            if arr[i][j+1] == 1:
                val-=1
                
            return val
        
        perm = 0
        
        rmax = len(grid)
        cmax = len(grid[0])
        
        grid_maxima = [[0] + i + [0] for i in grid]
        grid_maxima = [[0] * (cmax+2)] + grid_maxima + [[0] * (cmax+2)]
        
        for i in range(1, rmax+1):
            for j in range(1, cmax+1):
                if grid_maxima[i][j] == 1:
                    perm += get_perimeter(grid_maxima, i, j)
            
        
        return perm
