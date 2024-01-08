from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        print("In fun (start) : " + hex(id(nums)))
        for i in range( 1 , len(nums)):
            if  nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
        print("In fun (end) : " + hex(id(nums)))
        print(nums)
        return k
nums = [1,1,2,2,2,2,3]
print("Out fun (end) : " + hex(id(nums)))
sol = Solution()
result = sol.removeDuplicates(nums)
print("Out fun (end) : " + hex(id(nums)))
print(result)
print(nums)