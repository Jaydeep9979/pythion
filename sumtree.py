def isleaf(node):
    if not node:
        return False
    if not node.right and not node.left:
        return True
    else:
        return False
        

def issum_tree(node):
    if not node or (not node.left and not node.right):
        return True
    if issum_tree(node.left) and issum_tree(node.right):
        if not node.left:
            left=0
        elif isleaf(node.left):
            left=node.left.val
        else:
            left=2*(node.left.val)
        if not node.right:
            right=0
        elif isleaf(node.right):
            right=node.right.val
        else:
            right=2*(node.right.val)
        if node.val==(left+right):
            return True
        else:
            return False
    return False

issum_tree(root)

                 

             