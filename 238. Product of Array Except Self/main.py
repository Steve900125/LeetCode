from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        # Product of prifix, suffix, result
        prifix_list = [1]*nums_len
        suffix_list = [1]*nums_len
        result_list = []
        
        for loc in range(1, nums_len):
            prifix_list[loc] = prifix_list[loc-1]*nums[loc-1]
            suffix_list[nums_len-loc-1] = suffix_list[nums_len-loc]*nums[nums_len-loc]
        
        for loc in range(nums_len):
            result_list.append(prifix_list[loc]*suffix_list[loc])
        
        return result_list    

if __name__ == "__main__":
    nums = [2,2,3,4]
    s = Solution()
    print(s.productExceptSelf(nums))