class Solution:
    def combine(self, n, k):
        ans=[]
        
        def helper(curr,idx):
            if len(curr)==k:
                ans.append(curr)
                return
        
            for i in range(idx,n+1):
                if len(curr)>k:
                    break
                
                helper(curr+[i],i+1)
        helper([],1)
        
        return ans
        