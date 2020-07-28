class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #New dictionary
        d={}
        
        for i in range(len(nums)):
            #temporary variable
            temp=target-nums[i]
            #checking if it exists in dict
            if temp in d:
                return i,d[temp]
            #storing each element as key and its index as value
            d[nums[i]]=i
        
        return 0