class Solution:
    def isValidBST(self, root):
        def help(node,lower=float('-inf'),upper=float('inf')):
            if not node:
                return True
            
            val=node.val
            if val<=lower or val>=upper:
                return False
            
            if not help(node.right,val,upper):
                return False
            if not help(node.left,lower,val):
                return False
            return True
        
        return help(root)