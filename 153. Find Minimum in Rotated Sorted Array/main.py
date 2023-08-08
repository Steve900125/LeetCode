from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while True:

            mid = int(len(nums) // 2 ) 


            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                if nums[0] > nums[1]:
                    return nums[1]
                else :
                    return nums[0]
            
            # We have left_pointer (far-left) and right_pointer (far-right)
            # =============================================================
            # If the minimum value at letf side (contain middle one)
            # condition will be like : 
            # 1. mid < far-left and mid < far-right
            # 2. mid >  far-left and mid < far-left (Ascending order )
            # =============================================================
            # If the minimum value at right side (without middle one)
            # condition will be like :
            # 1. mid > far-left and mid > far-right
            # =============================================================            
            if nums[mid] > nums[left_pointer] and nums[mid] > nums[right_pointer]:
                left_pointer =  mid + 1                             
                nums = nums[ left_pointer : right_pointer + 1]
                right_pointer = len(nums) - 1
                left_pointer = 0
            else:
                right_pointer =  mid 
                nums = nums[ left_pointer : right_pointer + 1]


sol = Solution()
nums = [4,5,6,7,0,1,2]
result = sol.findMin(nums)
print(result)

