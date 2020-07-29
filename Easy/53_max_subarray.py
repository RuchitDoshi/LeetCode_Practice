class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algorithm
        max_num=nums[0]
        max_global=nums[0]
        
        for i in range(1,len(nums)):
            max_num=max(nums[i],max_num+nums[i])
            max_global=max(max_global,max_num)
        
        return max_global