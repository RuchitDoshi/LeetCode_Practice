class Solution:
    def threeSum(self, nums):
        nums.sort()
        l=len(nums)
        result=set()
        for i in range(l-2):
            if i!=0 and nums[i-1]==nums[i]:continue
            j=i+1
            k=l-1
            while(j!=k):
                temp=nums[i]+nums[j]+nums[k]
                if temp==0:
                    tu=tuple(sorted((nums[i],nums[j],nums[k])))
                    result.add(tu)
                if temp>0:
                    k-=1
                else:
                    j+=1
                
        return list(list(i) for i in result)
        
        
        