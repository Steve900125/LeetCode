from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_set = set()

        dic_zeor = {}
        dic_postive = {}
        dic_negative = {}

        for key in nums:
            if key == 0:
                if key in dic_zeor :
                    dic_zeor[key] += 1
                else :
                    dic_zeor[key] = 1
            elif key > 0:
                if key in dic_postive :
                    dic_postive[key] += 1
                else :
                    dic_postive[key] = 1
            elif key < 0:
                if key in dic_negative :
                    dic_negative[key] += 1
                else :
                    dic_negative[key] = 1
        # Situation 1 : 0 , 0 , 0
        if 0 in dic_zeor and dic_zeor[0] >=3 :
            ans_set.add((0,0,0))
        # Situation 2 : negative + postive  + 0  = 0 ( k ,-k , 0)
        if 0 in dic_zeor:
            for negative in dic_negative.keys():
                if -negative in dic_postive:
                    ans_set.add((negative,0,-negative))
        
        # Situation 3 : negative + negative + postive = 0
        
        keys_neg = list(dic_negative.keys())
        for neg_loc in  range(len(keys_neg)):
            # a + b = c and a != b
            a = keys_neg[neg_loc]
            for neg_inloc in range(neg_loc + 1 , len(keys_neg)):
                # part 1
                b = keys_neg[neg_inloc]
                c = -(a + b)
                if c in dic_postive:
                    ans_set.add(tuple(sorted([a,b,c])))
            # -k -k 2k
            # part 2
            if dic_negative[a] >= 2 and -(2 * a) in dic_postive:
                ans_set.add((a,a,-(2*a)))

        # Situation 4 : postive +  postive + negative = 0
        keys_pos = list(dic_postive.keys())
        for pos_loc in  range(len(keys_pos)):
            # a + b = c and a != b
            a = keys_pos[pos_loc]
            for pos_inloc in range(pos_loc + 1 , len(keys_pos)):
                # part 1
                b = keys_pos[pos_inloc]
                c = -(a + b)
                if c in dic_negative:
                    ans_set.add(tuple(sorted([a,b,c])))
            # -k -k 2k
            # part 2
            if dic_postive[a] >= 2 and -(2 * a) in dic_negative:
                ans_set.add((-(2 * a) , a , a))
        return [list(tuple_ans) for tuple_ans in list(ans_set)]


nums = [3,0,-2,-1,1,2]
sol = Solution()
result = sol.threeSum(nums)
print(result)