class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        if len(strs) == 0:
            return result
        
        min_size=[]
        for i in strs:
            min_size.append(len(i))
        
        
        counter=0
        while(counter < min(min_size)):
            num=0
            for i in range(len(strs)):
                if strs[i][counter]==strs[0][counter]:
                    num+=1
            if num==len(strs):
                counter+=1
            else:
                break
        

        if counter>0:
            
            for i in range(counter):
                result+=strs[0][i]
        
        
        return result
            
        