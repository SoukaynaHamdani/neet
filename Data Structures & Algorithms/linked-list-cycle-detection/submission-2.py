# Definition for singly-linked list. 
# class ListNode: 
#     def __init__(self, val=0, next=None): 
#         self.val = val
#         self.next = next 
class Solution: 
    def hasCycle(self, head: Optional[ListNode]) -> bool: 
        """ Floyd's Tortoise and Hare match: 2 pointers plan :  slow moves 1 step      fast moves 2 steps . if cycle they meet 
        o(n)time o(1)space """ 
        slow=head 
        fast=head 
        while  fast and fast.next:
            slow=slow.next 
            fast=fast.next.next 
            if fast==slow:
                return True
        return False