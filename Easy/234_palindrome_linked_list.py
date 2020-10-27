def isPalindrome(head):
    if head==None:
        return True
    
    stack=[]
    
    ptr1=head
    while(ptr1!=None):
        stack.append(ptr1.val)
        ptr1=ptr1.next
    
    if stack==stack[::-1]:
        return True
        
    
    return False