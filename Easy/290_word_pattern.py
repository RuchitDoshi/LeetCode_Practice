class Solution:
    def wordPattern(self, pattern, s):
        d={}
        st=s.split()
        if len(pattern)!=len(st):
            return False
        dt=[i for i in pattern]
        if len(set(dt))!=len(set(st)):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]]=st[i]
            else:
                if d[pattern[i]]!=st[i]:
                    return False
        return True