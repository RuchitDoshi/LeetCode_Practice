class Solution:
    def reverseWords(self, s):
        s_split=s.split()
        if len(s_split)==0:
            return ""
        result=s_split[-1]
        if len(s_split)>1:
            for i in range(len(s_split)-2,0,-1):
                result+=" "
                result+=s_split[i]
                
            result+=" "
            result+=s_split[0]
        
        return result