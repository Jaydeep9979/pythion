class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        def validate(root,minval=float("-inf"),maxval=float('inf')):
            if not root:
                return True
            if root.val<=minval or root.val>=maxval:
                return False
            return  validate(root.left,minval,root.val) and validate(root.right,root.val,maxval)
            
                
            
            
            


