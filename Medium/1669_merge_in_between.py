class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        t1=list1
        count=0
        while(count<(a-1)):
            t1=t1.next
            count+=1
        
        t2=t1
        while(count<b):
            t2=t2.next
            count+=1
        t2=t2.next
        t1.next=list2
        while(t1.next!=None):
            t1=t1.next
        t1.next=t2
        
        return list1