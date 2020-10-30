class Solution:
    def __init__(self):
        self.result=[]
    def helper(self,root):
        if root==None:
            return 
        self.helper(root.left)
        self.helper(root.right)
        self.result.append(root.val)
        
    def postorderTraversal(self, root):
        self.helper(root)
        return self.result