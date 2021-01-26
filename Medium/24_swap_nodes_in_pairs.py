# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        
        one=head
        two=one.next
        head=two
        while one!=None and two!=None:
            temp=two.next
            two.next=one
            one.next=temp
            
            ptr=one
            one=one.next
            if one==None:
                break
            
            two=one.next
            if two!=None:
                ptr.next=two
            else:
                ptr.next=one
                break
            
        return head