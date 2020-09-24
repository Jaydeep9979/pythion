# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue=collections.deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            node.left,node.right=node.right,node.left
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return root 
            
        
        # def invert(root):
        #     if not root:
        #         return 
        #     root.left,root.right=root.right,root.left
        #     if root.left:
        #         invert(root.left)
        #     if root.right:
        #         invert(root.right)    
            
        # invert(root)
        # return root
        