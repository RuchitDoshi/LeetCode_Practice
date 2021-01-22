class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        d={0:0,1:0,2:0}
        
        for i in range(len(nums)):
                d[nums[i]]+=1
        count=0
        for d,v in d.items():
            for j in range(v):
                nums[count]=d
                count+=1