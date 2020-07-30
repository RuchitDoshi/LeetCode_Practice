class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)==0:
            return 0
        left=0
        right=0
        sub=[]
        
        for i in range(len(s)):
            if s[i]=='(':
                left+=1
            else:
                right+=1
            
            if left==right:
                sub.append(left+right)
            
            if right>left:
                left=0
                right=0
        left=0
        right=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==')':
                right +=1
            else:
                left+=1
            
            if left==right:
                sub.append(left+right)
            
            if left>right:
                left=0
                right=0
        
        if len(sub)==0:
            return 0
        return max(sub)
            
            
            
        