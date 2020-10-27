class Solution:
      def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        def f(root):
            if not root.children: return 1
            h = -1
            for v in root.children:
                h = max(h, f(v))
            return 1 + h
        return f(root)