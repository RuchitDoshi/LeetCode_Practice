class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        result=[[1]]
        if rowIndex==0:
            return [1]        
        result.append([1,1])
        if rowIndex==1:
            return result[1]
        
        for i in range(2,rowIndex+1):
            temp=[]
            temp.append(1)
            for j in range(1,len(result[i-1])):
                temp.append(result[i-1][j-1]+result[i-1][j])
            temp.append(1)
            result.append(temp)
            
        return result[-1]