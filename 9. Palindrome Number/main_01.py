class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        
        if (len(x) % 2) == 0:
            for dis in range(len(x)/2):
                if x[dis] != x[ (len(x) - 1) - dis]:
                    return False
        else:
            for dis in range((len(x)//2 + 1)):
                if x[dis] != x[ (len(x) - 1) - dis]:
                    return False
        return True