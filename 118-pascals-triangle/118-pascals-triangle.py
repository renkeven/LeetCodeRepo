class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        loop, base case 1
        """
        
        def next_from_prev(arr):
            tmp = []
            for i in range(len(arr) - 1):
                tmp.append(arr[i] + arr[i+1])
            return [1] + tmp + [1]
                
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1], [1,1]]
        
        base = [[1], [1,1]]
        
        for j in range(numRows - 2):
            base.append(next_from_prev(base[j + 1]))
        
        return base