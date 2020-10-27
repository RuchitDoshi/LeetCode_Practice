class Solution:
    def detectCycle(self, head):
        if head==None:
            return head
        new_set=set()
        
        while(head!=None):
            if head in new_set:
                return head
            else:
                new_set.add(head)
                head=head.next
        
        return None