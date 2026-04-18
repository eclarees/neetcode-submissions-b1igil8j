# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False
        seen = []
        cur = head


        while cur.next: 
            if cur.val in seen:
                return True
            seen.append(cur.val)
            cur = cur.next 
        return False
            
        