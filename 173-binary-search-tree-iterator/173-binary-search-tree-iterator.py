# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder_arr = []
        self.inorderTree(root)
        self.pointer = -1
        
    def next(self) -> int:
        self.pointer += 1
        if len(self.inorder_arr) > self.pointer:
            return self.inorder_arr[self.pointer]
        return
            
    def hasNext(self) -> bool:
        if len(self.inorder_arr) > self.pointer + 1:
            return True
        else:
            return False
        
    def inorderTree(self, root) -> list:
        if root:        
            self.inorderTree(root.left)
            self.inorder_arr.append(root.val)
            self.inorderTree(root.right)
        return 


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()