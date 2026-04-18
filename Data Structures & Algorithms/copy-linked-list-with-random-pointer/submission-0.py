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
        cur = head
        hashmap = {} 

        while cur:
            new_node = Node(cur.val,None,None)
            hashmap[cur] = new_node 
            cur = cur.next 
        for old_node, new_node in hashmap.items():
            if old_node.random:
                new_node.random = hashmap[old_node.random]
            else:
                new_node.random = None 
            
            if old_node.next:
                new_node.next = hashmap[old_node.next]
            else:
                new_node.next = None
            
        return hashmap.get(head)
        
        
