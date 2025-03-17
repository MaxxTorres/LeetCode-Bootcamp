# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow_node = head
        fast_node = head

        # Find middle
        while fast_node and fast_node.next and fast_node.next.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        if fast_node and fast_node.next:
            mid_node = slow_node.next #odd
        else:
            mid_node = slow_node #even

        # Reverse second half
        curr = mid_node
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Compare both halves 
        curr_front = head
        curr_back = prev
        while curr_front != mid_node:
            if curr_front.val != curr_back.val:
                return False
            curr_front = curr_front.next
            curr_back = curr_back.next

        return True


        