# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """same as preorder, but goes from left-root-right"""
        
        in_list = []
        
        def inorder(root, list_):
            if root:
                #keep going left until it cannot
                inorder(root.left, list_)
                list_.append(root.val)
                inorder(root.right, list_)
            return
        
        inorder(root, in_list)
        
        return in_list