class Solution:
    def integerBreak(self, n):
        if n==2:
            return 1
        elif n==3:
            return 2
        elif n==4:
            return n
        else:
            x=int(n/3)
            y=(n-3*x)/2
            
            if 1>y>0:
                y=2
                x=x-1
            return int((3**x)*(2**y))