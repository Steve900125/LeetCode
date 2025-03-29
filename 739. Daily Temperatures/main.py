from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Stack stores pairs: (temperature, index)

        for i, current_temp in enumerate(temperatures):
            # While the current temperature is higher than stack top
            while stack and current_temp > stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append((current_temp, i))

        return answer
