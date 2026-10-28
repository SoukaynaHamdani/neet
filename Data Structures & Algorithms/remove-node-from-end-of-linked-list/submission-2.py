# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            """FIXED GAP: 2 pointers slow points at dummmy and fast is n steps ahead,while fast and fast.next both move 1 step at a time. Then slow is at the node before the nth node we need to delete  """
            dummy=ListNode(0) 
            dummy.next=head
            s=dummy 
            f=dummy
            while n>0:
                f=f.next
                n-=1
            while f and f.next: 
                s=s.next 
                f=f.next 
            s.next=s.next.next
            return dummy.next 
