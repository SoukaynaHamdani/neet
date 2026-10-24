# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode()
        curr1=l1  
        curr2=l2  
        curr=dummy 

        while curr1 and curr2: 
            if curr2.val > curr1.val:
                curr.next=curr1
                curr1 =curr1.next
            else:
                curr.next=curr2
                curr2 =curr2.next
            curr=curr.next
        
        if curr1:
            curr.next=curr1 
        elif curr2:
            curr.next=curr2
             
        return dummy.next

