from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # loop to target number
        end_point = len(numbers) - 1
    
        # find start point
        for small in range(len(numbers)):
            left = small + 1
            right = end_point
            temp_target = target - numbers[small]

            # BINARY SEARCH
            while left <= right :    
                mid = int((left + right)/2)
                print("mid {}".format(mid))
                print("left {}".format(left))
                print("right {}".format(right))
                if numbers[mid] > temp_target:
                    right = mid - 1
                elif numbers[mid] < temp_target:
                    left = mid + 1
                else:
                    return [small+1 , mid+1]
                
a = [2,7,11,15]
t = 9

sol = Solution()
ans = sol.twoSum(numbers=a,target=t)

print(ans)
        