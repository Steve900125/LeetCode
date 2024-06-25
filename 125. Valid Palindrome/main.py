class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        temp = s.lower()
        s = ''
        for i in temp:
            if i.isalpha() == True:
                s = s.join(i)

        print(s)
        if len(s) == 0:
            return True
        # check odd or even
        if len(s) % 2 == 0:
            mid = len(s) / 2
            print(s[0:mid],s[-1:(mid-1):-1])
            if s[0:mid] == s[-1:(mid-1):-1]:
                return True
        else :
            mid = len(s) // 2
            print(s[0:mid],s[-1:(mid):-1])
            if s[0:mid] == s[-1:(mid):-1]:
                return True
        
        return False

sol = Solution()
s = "race a car"

res = sol.isPalindrome(s)
print(res)
