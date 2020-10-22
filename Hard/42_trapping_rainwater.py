class Solution:
    def trap(self, height):
        if len(height)==0:
            return 0
        max_value=height[0]
        result=0
        for i in range(len(height)):
            
            if i!=(len(height)-1) and max_value>(max(height[i+1:])):
                max_value=max(height[i+1:])
            if max_value<height[i]:
                max_value=height[i]
            result+=(max_value-height[i])
            
        if max_value>height[-1]:
            result+=height[-1]-max_value
        return result