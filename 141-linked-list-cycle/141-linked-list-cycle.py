# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        hash_table = set()
        
        while head:
            if id(head) in hash_table:
                return True
            else:
                hash_table.add(id(head))
                
            head = head.next

        # for _ in range(20):
        #     print(id(head))
        #     head = head.next
          
        # while head:
        #     if id(head) >= id(head.next):
        #         print(id(head), id(head.next), head.next)
        #         if head.next == None:
        #             return False
        #         else:
        #             return True
        #     head = head.next
            
        return False