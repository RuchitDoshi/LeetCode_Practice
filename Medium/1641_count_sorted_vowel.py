class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n==1:
            return 5
        else:
            arr=[1,2,3,4,5]
            
            for i in range(2,n):
                for i in range(1,5):
                    arr[i]=arr[i]+arr[i-1]
                    
            
            return sum(arr)