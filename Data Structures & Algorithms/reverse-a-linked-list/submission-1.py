# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #two pointers approach 
        curr , prev = head , None

        while curr: #iterating full LL
              temp = curr.next
              curr.next = prev
              prev = curr
              curr = temp

        return prev      

             
             



  





















