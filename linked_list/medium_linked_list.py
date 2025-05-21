# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head):
        if head is None:
            return None

        slow, fast = head, head.next

        #find the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #split the list in half
        second = slow.next #second half of the list
        prev = slow.next = None #break the link of the first half from second

        #reverse the 2nd portion of the list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #merge lists
        first , second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2
            
