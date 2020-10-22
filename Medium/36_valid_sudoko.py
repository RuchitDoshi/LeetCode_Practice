class Solution:
    def isValidSudoku(self, board):
        
        counter=0
        j=0
        while(counter<9):
            rows={}
            cols={}
            for i in range(9):
                if board[counter][i] !=".":
                    if board[counter][i] in rows:
                        return False
                    else:
                        rows[board[counter][i]]=1
                if board[i][counter] !=".":
                    if board[i][counter] in cols:
                        return False
                    else:
                        cols[board[i][counter]]=1
            counter+=1
        
        
        for w in range(0,9,3):
            for k in range(0,9,3):
                sub={}
                for i in range(w,w+3):
                    for j in range(k,k+3): 
                        if board[i][j]!=".":
                            if board[i][j] in sub:
                                return False
                            else:
                                sub[board[i][j]]=1
                                
        
        return True
                
        
        
        