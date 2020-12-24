class Solution:
    def divide(self, dividend, divisor):
        if dividend==0:
            return 0
        
        if divisor ==1 or divisor==-1:
            temp=dividend*divisor
            if temp > (2**31-1):
                return 2**31 -1
            elif temp < (-2**31):
                return -2**31
            else:
                return temp
        
        i=int(exp(log(abs(dividend))-log(abs(divisor))))
        print(i)

        
        if dividend*divisor >0:
            if (i) > (2**31-1):
                return 2**31 -1
            else:
                return (i)
        else:
            if -(i) <(-2**31):
                return (-2**31)
            else:
                return -(i)
        