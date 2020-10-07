class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def issame(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val==node2.val and issame(node1.left,node2.left) and issame(node1.right,node2.right)
        stack=[s]
        while stack:
            new=[]
            for root1 in stack:
                if root1.val==t.val:
                    if issame(root1,t):
                        return True
                if root1.left:
                    new.append(root1.left)
                if root1.right:
                    new.append(root1.right)
            stack=new
        return False
        