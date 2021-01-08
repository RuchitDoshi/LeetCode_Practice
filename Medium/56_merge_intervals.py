class Solution:
    def merge(self, intervals):
        intervals.sort()
        result=[]
        n=len(intervals)
        i=0
        while(i<n):
            start=intervals[i][0]
            end=intervals[i][-1]
            j=i+1
            for j in range(i+1,n):
                if intervals[j][0]<=end and intervals[j][-1]>end:
                    end=intervals[j][-1]
                    i+=1
                elif intervals[j][-1]<=end:
                    i+=1
                else:
                    break
            result.append([start,end])
            i+=1
        
        
        return result
                
        