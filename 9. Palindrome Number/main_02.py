class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        half_len_x = int(len(x)/2)
        if (len(x) % 2) == 0:
            if x[0:half_len_x] != x[len(x)-1:half_len_x - 1:-1]:
                return False
        else:
            if x[0:half_len_x] != x[len(x)-1:half_len_x:-1]:
                return False
        return True