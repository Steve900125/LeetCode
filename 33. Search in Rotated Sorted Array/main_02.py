# Record : Not best sloution 
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Part 1 : Find minimum number
        min_found = False
        min_loc = None
        # condition of find minimum

        left_pointer = 0
        right_pointer = len(nums) - 1


        while not min_found:
            # Now middle location
            mid = int((left_pointer + right_pointer) // 2) 

            # Find minimum 2 situation
            # Otherwise, it indicates that the search is ongoing
            # 1. If the nums n == 1 which means the only number is the minimum value
            if left_pointer == right_pointer:
                min_found = True
                min_loc = left_pointer
            # 2. If pointers are adjacent that set the min_loc
            elif (right_pointer - left_pointer) == 1 :
                if nums[right_pointer] > nums[left_pointer]:
                    min_loc = left_pointer
                else :
                    min_loc = right_pointer
                min_found = True
            else :
                # If didn't find min_loc
                if nums[mid] > nums[left_pointer] and nums[mid] > nums[right_pointer]:
                    left_pointer = mid + 1
                else :
                    right_pointer = mid 

        # Part 2 : Find target
        # nums[min_loc] is the minimum number in nums
        # Therefore, the target can't be smaller than nums[min_loc].
        if target < nums[min_loc]:
            return -1
        else : 
            location = min_loc + (target - nums[min_loc])
            if location < len(nums):
                for ans_loc in range(min_loc,location + 1,1):
                    if nums[ans_loc] > target:
                        return -1
                    if nums[ans_loc] == target:
                        return ans_loc

            if location >= len(nums) :
                for ans_loc in range(min_loc,len(nums),1):
                    if nums[ans_loc] > target:
                        return -1
                    if nums[ans_loc] == target:
                        return ans_loc

                for ans_loc in range(min_loc):
                    if nums[ans_loc] > target:
                        return -1
                    if nums[ans_loc] == target:
                        return ans_loc
            return -1

nums = [3,5,1]
target= 5
sol = Solution()
result = sol.search(nums , target)  
print(result)   


