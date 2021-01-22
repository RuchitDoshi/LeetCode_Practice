class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def helper(curr,idx):
            if sum(curr)==target:
                ans.append(curr)
                return
            
            for i in range(idx,len(candidates)):
                if sum(curr)+candidates[i]>target:
                    break
                helper(curr+[candidates[i]],i)
        helper([],0)
        
        return ans