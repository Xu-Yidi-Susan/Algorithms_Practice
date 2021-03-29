# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        dummy = ListNode(0,head)
        cur = dummy

        while cur.next.next:
            if cur.next.val != cur.next.next.val:
                cur = cur.next
            else:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
                if not cur.next:
                    return dummy.next
                  
        return dummy.next
