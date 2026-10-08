# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head              # base case     
        newHead = self.reverseList(head.next)
        head.next.next = head        # هنا كنعكسو الرابط
        head.next = None
        return newHead