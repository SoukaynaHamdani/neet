# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        match: HASH MAP / HASH SET
        plan : Traverse the linked list and store visited nodes. 
               If we encounter a node already in our set, a cycle exists.
        o(n)time o(n)space
        """
        seen=set()
        curr=head 
        while curr:
            if curr in seen:
                return True 
            seen.add(curr)
            curr=curr.next
        return False