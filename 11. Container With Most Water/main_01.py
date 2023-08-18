# Bad : Time Limit Exceeded
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # len(height) ^ 2 - len(height) = record size
        ans = -1
        for out_loc in range(len(height)):
            for in_loc in range(out_loc):
                if height[out_loc] > height[in_loc]:
                    contain_water = height[in_loc] * (out_loc - in_loc)
                    
                else:
                    contain_water = height[out_loc] * (out_loc - in_loc)

                ans = max(contain_water , ans)
        return ans
# 用矩陣的位置和數值去算 O(n^2) 
# 可能與座標有關聯 2座標以較低的座標為高來計算面積