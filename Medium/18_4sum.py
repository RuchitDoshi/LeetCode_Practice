class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        l=len(nums)
        result=set()
        for i in range(l-3):
            for j in range(i+1,l-2):
                k=j+1
                w=l-1
                while(w!=k):
                    d=nums[i]+nums[j]+nums[k]+nums[w]
                    if d==target:
                        temp=tuple(sorted((nums[i],nums[j],nums[k],nums[w])))
                        result.add(temp)
                    if d>target:
                        w-=1
                    else:
                        k+=1
        
        return list(list(i) for i in result)
                