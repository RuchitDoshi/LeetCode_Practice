class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        count1=0
        count2=0
        
        for i in range(len(num1)):
            count1+=(ord(num1[i])-ord('0'))*(10**(len(num1)-i-1))
        
        for i in range(len(num2)):
            count2+=(ord(num2[i])-ord('0'))*(10**(len(num2)-i-1))
        
        return str(count1*count2)