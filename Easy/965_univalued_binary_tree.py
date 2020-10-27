class Solution:
    def isUnivalTree(self, root):
        def helper(root,val):
            if root==None:
                return True
            if root.val!=val:
                return False
            if not helper(root.left,root.val):
                return False
            if not helper(root.right,root.val):
                return False
            return True
        return helper(root,root.val)