class Solution:
    def findRepeatedDnaSequences(self, s):
        result=set()
        
        hashmap={}
        
        for i in range(len(s)):
            temp=s[i:i+10]
            
            if temp in hashmap:
                result.add(temp)
            else:
                hashmap[temp]=1
        
        return list(result)