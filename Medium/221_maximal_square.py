class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        a=min(m,n)
        for size in range(a,0,-1):
            h=m-size+1
            w=n-size+1
            for x in range(h):
                for y in range(w):
                    i=x
                    j=y
                    count=0
                    for t in range(size**2):
                        if j==(y+size):
                            j=y
                            i+=1
                        if matrix[i][j]=='0':
                            break
                        j+=1
                        count+=1
                    if count==(size**2):
                        return count
            
        return 0        