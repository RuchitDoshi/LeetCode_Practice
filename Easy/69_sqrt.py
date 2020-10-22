class Solution:
    def mySqrt(self, x: int) -> int:
        count=1
        s=int(x/2)
        while(count<s):
            if count*count > x:
                break
            count+=1
        
        if (count*count)>x:
            return count-1
        else:
            return count