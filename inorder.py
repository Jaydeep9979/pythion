class Solution:
    def isOrder(self, root: TreeNode) -> bool:
        if not root:
            return []
        stack=[]
        inorder=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            if stack==[]:
                break
            root=stack.pop()
            inorder.append(root.val)
            root=root.right
        


