# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root==None:
            return []
        result=[]
        
        def helper(curr,root):
            curr+=(root.val,)
            if sum(list(curr))==targetSum and root.left==None and root.right==None:
                result.append(list(curr))
 
            if root.left:
                helper(curr,root.left)
            if root.right:
                helper(curr,root.right)
            
            return
        
        
        helper(tuple(),root)
        
        return result
        