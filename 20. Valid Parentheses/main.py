class Solution:
    def isValid(self, s: str) -> bool:

        # brackets types
        left =  {'(': ')', '{': '}', '[': ']'}
        right = { ')':'(', '}':'{', ']':'['}
        stack = []

        for i in range(0,len(s)):
            if s[i] in left:
                stack.append(s[i])
                print(stack)
            elif s[i] in right and  len(stack) != 0:
                if right[s[i]] == stack[-1]:
                    stack.pop()
                    print(stack)
                else:
                    print(stack)
                    return False
            else:
                return False
                
        if len(stack) == 0:
            print(stack)
            return True
        else:
            print(stack)
            return False


s = "{[]}"
sul = Solution()
res = sul.isValid(s=s)
print(res)