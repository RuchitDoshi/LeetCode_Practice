class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        visited=[[0]*n for _ in range(n)]
        
        ns=0
        ne=n-1
        count=1
        while count<=(n**2):
            
            for i in range(ns,ne+1):
                if visited[ns][i]==0:
                    visited[ns][i]=count
                    count+=1

            for j in range(ns+1,ne+1):
                if visited[j][ne]==0:
                    visited[j][ne]=count
                    count+=1

            for k in range(ne-1,ns-1,-1):
                if visited[ne][k]==0:
                    visited[ne][k]=count
                    count+=1

            for w in range(ne-1,ns,-1):
                if visited[w][ns]==False:
                    visited[w][ns]=count
                    count+=1
            
            ns+=1
            ne-=1
        
        return visited

        