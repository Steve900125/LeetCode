class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums) 
        max_len = 0

        while nums_set: 
            num = nums_set.pop()  
            current_len = 1

            left = num - 1
            while left in nums_set:
                nums_set.remove(left)
                left -= 1
                current_len += 1

            right = num + 1
            while right in nums_set:
                nums_set.remove(right)
                right += 1
                current_len += 1
                
            max_len = max(max_len, current_len)

        return max_len
        