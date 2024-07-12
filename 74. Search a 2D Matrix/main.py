from typing import List
# wrong answer
class Solution:

    def col_to_index(self, target_high, target_width, width_max):
        return target_high*width_max + target_width
    
    def index_to_col(self, index, width_max):
        if width_max != 0:
            target_width = index % width_max
        else :
            target_width = 0
        target_high = (index - target_width)/width_max
        return target_high, target_width

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        matrix_high = len(matrix) - 1 
        matrix_width = len(matrix[0]) - 1

        left = {'high':0 ,'width':0}
        right = {'high':matrix_high ,'width':matrix_width}
        mid = {}

        while self.col_to_index(left['high'], left['width'], matrix_width) <= self.col_to_index(right['high'], right['width'], matrix_width):
            sum_index = self.col_to_index(left['high'], left['width'], matrix_width) + self.col_to_index(right['high'], right['width'], matrix_width)
            mid['high'], mid['width'] = self.index_to_col(sum_index // 2, matrix_width)

            if matrix[mid['high']][mid['width']] < target:
                left['high'], left['width'] = self.index_to_col(sum_index // 2 + 1, matrix_width)
            elif matrix[mid['high']][mid['width']] > target:
                right['high'], right['width'] = self.index_to_col(sum_index // 2 - 1, matrix_width)
            else :
                return True
        
        return False