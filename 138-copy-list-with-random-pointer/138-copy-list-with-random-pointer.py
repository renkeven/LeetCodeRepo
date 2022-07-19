"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """construct a hash map of pointers using id"""
        
        hash_map = dict()
        
        copy_list = Node(0)
        copy_head = copy_list
        
        random_head = head
        random_list = copy_list
        
        index = 0
        ran_counter = 0
        
        while head:
            """copy uni-directional link"""
            copy_head.next = Node(head.val)
            
            hash_map[id(head)] = (id(head.random), index)
            
            head = head.next
            copy_head = copy_head.next
            index += 1
            
        while random_head:
            cur_rand = random_head.random
            if cur_rand is None:
                random_list.next.random = None
            
            else:
                hash_iter = iter(hash_map)
                for _ in range(ran_counter):
                    next(hash_iter)
                key = next(hash_iter)
                
                if key in hash_map:
                    tmp_copy_list = copy_list.next
                    idx = hash_map[hash_map[key][0]][1]
                    for _ in range(idx):
                        tmp_copy_list = tmp_copy_list.next
                    random_list.next.random = tmp_copy_list          
                
            ran_counter += 1
            random_list = random_list.next
            random_head = random_head.next
            
        # while copy_list:
        #     print(copy_list, copy_list.val, copy_list.next, copy_list.random)
        #     copy_list = copy_list.next

        return copy_list.next
