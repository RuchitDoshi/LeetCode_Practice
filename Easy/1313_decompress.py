class Solution:
    def decompressRLElist(self, nums):
        result=[]
        for i in range(0,len(nums),2):
            result+= ([nums[i+1]]*nums[i])
        
        return result