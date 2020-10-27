class Solution:
    def searchInsert(self, nums):
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target<nums[i]:
                    return i
        
            
        return len(nums)