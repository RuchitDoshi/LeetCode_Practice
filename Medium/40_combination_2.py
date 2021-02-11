class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates)<target:
            return []
        
        result=[]
        candidates.sort()
        
        def helper(curr, idx):
            
            if sum(curr)==target:
                if curr not in result:
                    result.append(curr)
                return
            
            for j in range(idx+1,len(candidates)):
                if sum(curr+[candidates[j]])>target:
                    break
                
                helper(curr+[candidates[j]],j)
            
        
        for i in range(len(candidates)):
            helper([candidates[i]],i)
        
        return result
        