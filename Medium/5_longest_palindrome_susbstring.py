class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return s
        
        out=""
        for i in range(0,len(s)-1):
            for j in range(len(s)-1,i,-1):
                if len(out)>=j+1-i:
                    break
                elif s[i:j+1]==s[i:j+1][::-1]:
                        out=s[i:j+1]
                        break
        
        if len(out)==0:
            return s[0]
        
        return out
        