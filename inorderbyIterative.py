class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return []
        stack=[]
        inorder=[]
        prev=None
        while not root or not stack:
            while root:
                stack.append(root)
                root=root.left
            if stack==[]:
                break
            root=stack.pop()
            if prev!=None and root.val<=prev:
                return False
            prev=root.val    
            inorder.append(root.val)
            root=root.right
        return True

        


