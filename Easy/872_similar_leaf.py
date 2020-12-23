# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.l1=[]
        self.l2=[]
    def help(self,root,num):
        if root == None:
            return 
        if root.left==None and root.right==None:
            if num==1:
                self.l1.append(root.val)
            if num==2:
                self.l2.append(root.val)
        self.help(root.left,num)
        self.help(root.right,num)
            
    def leafSimilar(self, root1, root2):
        self.help(root1,1)
        self.help(root2,2)
        
        if self.l1==self.l2:
            return True
        
        return False