class Solution:
    def maxProduct(self, nums):
        if len(nums)==0:
            return 0
        first=nums.pop(0)
        smallest=first
        largest=first
        best=first
        
        for i in nums:
            s=min(i,i*largest,i*smallest)
            largest=max(i,i*largest,i*smallest)
            smallest=s
            best=max(best,largest,smallest)
        
        return best
        