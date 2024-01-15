from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash table dict
        hash_table = {}

        for loc in range(len(nums)):
            hash_table[nums[loc]] = loc

        for loc in range(len(nums)):
            if (target - nums[loc]) in hash_table and loc != hash_table[target - nums[loc]]:
                return [loc , hash_table[target - nums[loc]]]
        
        return []