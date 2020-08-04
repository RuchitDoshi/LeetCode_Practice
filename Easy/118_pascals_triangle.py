class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        result=[[1]]
        if numRows==1:
            return result
        
        result.append([1,1])
        if numRows==2:
            return result
        
        for i in range(3,numRows+1):
            temp=[]
            temp.append(1)
            for j in range(1,len(result[i-2])):
                temp.append(result[i-2][j-1]+result[i-2][j])
            temp.append(1)
            result.append(temp)
            
        return result