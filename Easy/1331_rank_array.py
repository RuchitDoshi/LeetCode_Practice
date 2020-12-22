class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d={}
        for i,j in enumerate(sorted(set(arr))):
            d[j]=i+1
        return [d[i] for i in arr]