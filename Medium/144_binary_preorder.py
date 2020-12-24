# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result=[]
    def help(self,root):
        self.result.append(root.val)
        if root!=None:
            if root.left!=None:
                self.help(root.left)
        if root!=None:
            if root.right!=None:
                self.help(root.right)
    def preorderTraversal(self, root):
        if root==None:
            return 
        self.help(root)
        return self.result
        