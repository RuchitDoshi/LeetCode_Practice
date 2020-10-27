class Solution:
    def getIntersectionNode(self, headA, headB)s:
        d={}
        
        while(headA):
            d[headA]=1
            headA=headA.next
        
        while(headB):
            if headB in d:
                return headB
            headB=headB.next