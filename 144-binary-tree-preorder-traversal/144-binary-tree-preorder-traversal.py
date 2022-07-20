# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        
        def root_visit(root, list_):
            if root:
                list_.append(root.val)
                root_visit(root.left, list_)
                root_visit(root.right, list_)
            
            return
        
        root_visit(root, preorder)
        
        return preorder
        
                