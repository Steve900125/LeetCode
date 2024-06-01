from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for i in nums :
            if i in hash_table:
                hash_table[i] += 1
            if not i in hash_table:
                hash_table[i] = 1
        sorted_items = sorted(hash_table.items(), key = lambda x: x[1] , reverse=True)
            
        return [item[0] for item in sorted_items[:k]]