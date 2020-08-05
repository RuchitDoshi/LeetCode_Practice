class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        
        for i in range(len(s)):
            if s[i] in dict1:
                dict1[s[i]].append(i)
            else:
                dict1[s[i]]=[i]
            
            if t[i] in dict2:
                dict2[t[i]].append(i)
            else:
                dict2[t[i]]=[i]
        
        s_keys=list(dict1.keys())
        t_keys=list(dict2.keys())
        
        for i in range(len(dict1)):
            if dict1[s_keys[i]] != dict2[t_keys[i]]:
                return False  
        return True       