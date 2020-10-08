class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        inorder=[]
        prev=float('-inf')
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack:
                break
            root=stack.pop()
            if prev>=root.val:
                return False
            prev=root.val
            root=root.right
        return True
            
            
            


