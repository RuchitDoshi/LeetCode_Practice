class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        if len(A)==0:
            return 0
        n=len(A)
        s=sum([A[i]*i for i in range(n)])
        t=sum(A)
        res=s
        for i in range(n-1):
            s=s-t+A[i]*(n)
            if s>=res:
                res=s
            
        return res