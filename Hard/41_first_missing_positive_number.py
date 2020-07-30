class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 1
    
        
        if max(nums)<=0:
            return 1
        
        
        for i in range(1,max(nums)):
            if i in nums:
                continue
            else:
                return i
        

        
        return max(nums)+1
        
        