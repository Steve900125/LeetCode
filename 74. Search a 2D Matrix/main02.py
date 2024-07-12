from typing import List
class Solution:
    def col_to_index(self, row, col, num_cols):
        return row * num_cols + col
    
    def index_to_col(self, index, num_cols):
        row = index // num_cols
        col = index % num_cols
        return row, col

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        left = 0
        right = num_rows * num_cols - 1

        while left <= right:
            mid = (left + right) // 2
            mid_row, mid_col = self.index_to_col(mid, num_cols)

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False