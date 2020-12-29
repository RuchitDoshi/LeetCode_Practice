# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self,root,s,sum):
        if root==None:
            return False
        s+=root.val
        if root.left==None and root.right==None and s==sum:
                return True
        else:
            return self.help(root.left,s,sum) or self.help(root.right,s,sum)
                     
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:
            return False
        return self.help(root,0,sum)