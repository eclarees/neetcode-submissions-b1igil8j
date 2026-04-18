# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = ListNode() 
        tail=dummy
        cur1 = list1 
        cur2 = list2 

        # stop when either list become empty
        while cur1 and cur2:
            if cur1.val < cur2.val:
                tail.next=cur1 
                cur1 = cur1.next 
            else:
                tail.next = cur2
                cur2 = cur2.next 

            tail = tail.next 

        # find non empty list and insert into result
        if cur1:
            tail.next = cur1
        if cur2:
            tail.next=cur2

        return dummy.next 