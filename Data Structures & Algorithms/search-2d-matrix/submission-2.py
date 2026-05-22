class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            if target in matrix[i]:
                return True
        
        return False
