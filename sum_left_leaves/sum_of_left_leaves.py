class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(self, root: TreeNode) -> int:

    final_sum = 0

    if not root:
        return 0
        
    if root.left:
        if not root.left.left and not root.left.right:
            final_sum += root.left.val
        else:
            final_sum += self.sumOfLeftLeaves(root.left)
    final_sum += self.sumOfLeftLeaves(root.right)

    return final_sum