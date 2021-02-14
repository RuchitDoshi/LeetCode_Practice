class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        n=len(matrix[0])
        m=len(matrix)
        

        ms=0
        me=m-1
        
        ns=0
        ne=n-1
        
        visited=[[False]*n for _ in matrix]
        
        result=[]
        
        
        while ms<=me and ns<=ne:
        
            for i in range(ns,ne+1):
                if visited[ms][i]==False:
                    result.append(matrix[ms][i])
                    visited[ms][i]=True
                    
            for j in range(ms+1,me+1):
                if visited[j][ne]==False:
                    result.append(matrix[j][ne])
                    visited[j][ne]=True
            
            for k in range(ne-1,ns-1,-1):
                if visited[me][k]==False:
                    result.append(matrix[me][k])
                    visited[me][k]=True
            
            for w in range(me-1,ms,-1):
                if visited[w][ns]==False:
                    result.append(matrix[w][ns])
                    visited[w][ns]=True
            ms+=1
            me-=1
            
            ns+=1
            ne-=1
            
        
        return result