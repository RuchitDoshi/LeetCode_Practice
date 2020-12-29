class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort(reverse=True)
        result=0
        for i in range(len(citations)):
            if (i+1)<=citations[i]:
                result=i+1
            if (i+1)>citations[i]:
                break
        
        return result