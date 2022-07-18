# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
        
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#         merged_list = ListNode(min(list1.val, list2.val))
        
#         if list1.val <= list2.val:
#             list1 = list1.next
#         else:
#             list2 = list2.next
        
        #dummy is the whole list
        dummy = ListNode(0)
        #keeps track at the end of the list
        merged_list = dummy
    
        while (list1 and list2):
            if list1.val <= list2.val:
                merged_list.next = ListNode(list1.val)
                list1 = list1.next 
            else:
                merged_list.next = ListNode(list2.val)
                list2 = list2.next
            merged_list = merged_list.next

        if list1:
            merged_list.next = list1
            
        if list2:
            merged_list.next = list2
            
        #print(dummy, merged_list, list1, list2)
                
        return dummy.next