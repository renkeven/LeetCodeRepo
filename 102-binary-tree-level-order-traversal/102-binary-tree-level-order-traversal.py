# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        preorder = []

        def root_visit(root, list_, l=0):
            if root:
                if len(list_) < l+1:
                    list_.append([])
                    
                list_[l].append(root.val)
                
                root_visit(root.left, list_, l+1)
                root_visit(root.right, list_, l+1)
            
            return
        
        root_visit(root, preorder)
        
        return preorder
        