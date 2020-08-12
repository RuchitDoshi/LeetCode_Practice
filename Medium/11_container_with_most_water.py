class Solution:
    def maxArea(self, height) -> int:
        area=0
        head=0
        tail=len(height)-1
        
        while(head!=tail):
            if (height[head]  < height[tail]):
                temp=(tail-head)*(height[head])
                head+=1
            else:
                temp=(tail-head)*height[tail]
                tail-=1
            
            if temp > area :
                area=temp
        return area
                
        