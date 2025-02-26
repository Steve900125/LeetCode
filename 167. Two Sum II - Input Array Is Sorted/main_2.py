from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while True:
            sum = numbers[left] + numbers[right]

            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else :
                return [left+1, right+1]

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_p = 0
        right_p = len(numbers)-1

        while left_p <= right_p:
            sum_num = numbers[left_p]+numbers[right_p]
            if sum_num > target:
                right_p -= 1 
            elif sum_num < target:
                left_p += 1
            else:
                return [left_p+1, right_p+1]
