class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        i=0
        while(i<m):
            if obstacleGrid[i][0]==1:
                break
            else:
                obstacleGrid[i][0]=10
            i+=1
        
        i=0
        while(i<n):
            if obstacleGrid[0][i]==1:
                break
            else:
                obstacleGrid[0][i]=10
            i+=1
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    continue
                else:
                    
                    if obstacleGrid[i-1][j] !=1 and obstacleGrid[i][j-1]!=1:
                        obstacleGrid[i][j]= obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                
                    elif obstacleGrid[i-1][j] ==1 and obstacleGrid[i][j-1]!=1:
                        obstacleGrid[i][j]= obstacleGrid[i][j-1]
                
                               
                    elif obstacleGrid[i-1][j] !=1 and obstacleGrid[i][j-1] ==1:
                        obstacleGrid[i][j]= obstacleGrid[i-1][j]
                    
        
        return int(obstacleGrid[m-1][n-1]/10)