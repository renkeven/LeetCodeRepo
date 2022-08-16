# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check_tree(t1, t2):
            if t1 and t2:
                if t1.val == t2.val:
                    return check_tree(t1.left, t2.left) and check_tree(t1.right, t2.right)
                else:
                    return False
                
            if (not t1) and (not t2):
                return True
            
            else:
                return False
            
        return check_tree(p, q)