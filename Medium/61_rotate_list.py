# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if head==None or head.next==None:
            return head
        t=head
        l=0
        while(t!=None):
            t=t.next
            l+=1   
        for i in range(int(k%l)):
            t1=head
            while(t1.next.next!=None):
                t1=t1.next
            t2=t1.next
            t2.next=head
            head=t2
            t1.next=None
            
        return head
            
        