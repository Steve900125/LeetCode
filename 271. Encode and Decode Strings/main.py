from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        strs_merged = ''
        for item in strs:
            # 在每個字串前面加上長度和 '@' 分隔符號
            strs_merged += str(len(item)) + '@' + item  
        return strs_merged

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0  # 指針
        while i < len(s):
            num_end = s.find('@', i)  # 找到 '@' 位置
            if num_end == -1:
                break  # 防止找不到 '@' 時發生錯誤
            
            str_number = int(s[i:num_end])  # 取得字串長度
            start = num_end + 1  # '@' 後的起始索引
            end = start + str_number  # 計算結束索引
            
            strs.append(s[start:end])  # 擷取字串
            i = end  # 更新指針
        return strs