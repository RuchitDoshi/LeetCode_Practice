# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists)==0:
            return None
        
        
        self.heads=[lists[i] for i in range(len(lists)) if lists[i]!=None]
        self.vals=[lists[i].val for i in range(len(lists)) if lists[i]!=None]
        
        if len(self.heads)==0:
            return None
        
        min_val=min(self.vals)
        idx=self.vals.index(min_val)
        
        head=self.heads[idx]
        ptr=head
        
        self.heads[idx]=self.heads[idx].next
        
        
        if self.heads[idx]==None:
            self.heads.pop(idx)
            self.vals.pop(idx)
        else:
            self.vals[idx]=self.heads[idx].val
            
        
        
        while len(self.heads)!=0:
            
            min_val=min(self.vals)
            idx=self.vals.index(min_val)
            ptr.next=self.heads[idx]
            ptr=ptr.next
            
            self.heads[idx]=self.heads[idx].next
        
            if self.heads[idx]==None:
                self.heads.pop(idx)
                self.vals.pop(idx)
            else:
                self.vals[idx]=self.heads[idx].val
                
        return head
        
        
        