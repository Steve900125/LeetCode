from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_set = set()
        dic = {}
        # Dictionary to store:
        # 1. Key = value of nums[n]
        # 2. Value = Count of occurrences of "nums[n] value"

        for key in nums:
            if key in dic:
                dic[key] += 1
            else :
                dic[key] = 1
        
        # Situation 1 :  [0,0,0]
        if 0 in dic and dic[0] >= 3:
            ans_set.add((0,0,0))

        # Situation 2 : [k , -k , 0]
        # Situation 3 : [2k , -k , -k]
        # Situation 4 : [-2k , k , k]        
        for value,count in dic.items():
            # dic exist 0 and have k and -k
            if  0 in dic and (-value) in dic and -value != 0:
                ans_set.add(tuple(sorted([-value,0,value])))
            # dic exist 2 values = -k and 1 value = 2k
            if (-value) in dic and dic[(-value)] >= 2  and (2 * value) in dic and -value != 0:
                ans_set.add(tuple(sorted([-value,-value,2*value])))
            # dic exist 2 values = k and 1 value = -2k
            if value in dic and dic[value] >= 2  and (2 * -value) in dic and -value != 0:
                ans_set.add(tuple(sorted([value,value,2*-value])))
        # Situation 5 : set(a , b , c) and a + b = -c or b + c = -a or c + a = -b 
        keys = list(dic.keys())
        for key_loc in range(len(dic)):
            a = keys[key_loc]
            for key_inloc in range(key_loc + 1 , len(dic) , 1):              
                b = keys[key_inloc]
                c = a + b
                if - c in dic and a != -c and b != -c:
                    ans_set.add(tuple(sorted([a,b,-c])))
                    

        return [list(tuple_ans) for tuple_ans in list(ans_set)]
            


nums = [-1,0,1,2,-1,-4]
sol = Solution()
result = sol.threeSum(nums)
print(result)