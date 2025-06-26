# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
            

    def addTwoNumbers(self, l1 ,l2):
        # Create a dummy node to serve as the head of the result linked list
        res = ListNode()
        curr = res # Pointer to build the result list
        carry = 0 # Variable to store any carry-over value during addition


        while l1 or l2 or carry:
            # Get the current values from each list, or 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            #add the 2 values of the list and carry if applicable
            total = val1 + val2 + carry
            carry = total // 10 #find if there is overflow by dividing the total by 10 ex: 10/10 = 1
            digit = total % 10 # seperate the number if there is overflow such by 18%10 = 8

            #add the digit to the next node
            curr.next = ListNode(digit) 
            curr = curr.next


            #if there are any values left over in the lists, traverse and add them into the new list
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        #return the result linked list but to the next pointer since the head will be 0
        return res.next

