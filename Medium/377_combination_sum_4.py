class Solution:
    def combinationSum4(self, nums, target):
        nums.sort()
        arr=[0 for i in range(target+1)]
        arr[0]=1
        for i in range(1,target+1):
            for num in nums:
                if i < num:
                    break
                else:
                    arr[i]+=arr[i-num]
                    
        return arr[target]