class Solution:
    def __init__(self):
        self.ans=[]
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
            
        def dfs(node,count,arr):
            arr.append(node.val)
            count+=node.val
            if not node.right and not node.left:
                if count==sum:
                    self.ans.append(arr)
                return 
            if node.left:
                dfs(node.left,count,arr)
            if node.right:
                dfs(node.right,count,arr)
        arr=[]
        count=0
        dfs(root,count,arr)
        return self.ans

[5,4,8]
9