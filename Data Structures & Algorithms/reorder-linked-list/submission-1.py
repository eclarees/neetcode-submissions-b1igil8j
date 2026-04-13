# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        import math
        tail = head
        cur = head
        second = cur.next
        while tail.next!=None:
            tail = tail.next
        if cur==tail:
            return 

        while second!=tail: 
            cur.next= tail
            tail.next=second
            cur = second
            if cur.next==tail:
                cur.next = None 
                return 
            second = cur.next 
            newTail = cur
            while newTail.next!= tail:
                newTail = newTail.next
            tail = newTail
        tail.next = None
        

        
        
            
        