class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        
        word1_len = len(word1)
        word2_len = len(word2)

        for i in range(word1_len):
            if i > word2_len-1:
                ans = ans+word1[i:]
                break
            else:
                ans = ans + word1[i] + word2[i]
        
        if word2_len > word1_len:
            ans = ans + word2[word1_len:]
        
        return ans
            
        