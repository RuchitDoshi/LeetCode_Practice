class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n==0:
            return 0
        s=0
        while(s*s<=n):
            s+=1
        return s-1