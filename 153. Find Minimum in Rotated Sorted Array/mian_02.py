from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left_pointer = 0
        right_pointer = len(nums) - 1

        while True:
            # Now middle location
            mid = int((left_pointer + right_pointer) // 2) 

            # Find minimum 2 situation
            # Otherwise, it indicates that the search is ongoing
            # 1. If the nums n == 1 which means the only number is the minimum value
            if left_pointer == right_pointer:
                return nums[left_pointer]
            # 2. If pointers are adjacent that set the min_loc
            elif (right_pointer - left_pointer) == 1 :
                if nums[right_pointer] > nums[left_pointer]:
                    return nums[left_pointer]
                else :
                    return nums[right_pointer]
            else :
                # If didn't find min_loc
                if nums[mid] > nums[left_pointer] and nums[mid] > nums[right_pointer]:
                    left_pointer = mid + 1
                else :
                    right_pointer = mid