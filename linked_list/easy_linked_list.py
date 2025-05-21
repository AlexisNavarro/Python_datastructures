# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head):
        if head is None:
            return None

        prev, curr = None, head
        
        while curr is not None:
            
            #store the next value before breaking the link
            temp = curr.next

            #reverse the current node pointer, to point to the previous node
            curr.next = prev

            #move previous to the current 
            prev = curr

            #curr will move forward to the pointer we saved
            curr = temp
        return prev
    

    def mergeTwoLists(self, list1, list2):
        #Initialize a new linked list
        new_list = ListNode()

        #make the temp pointer node become the head for the new list
        temp = new_list

        #traverse both linked lists
        while list1 and list2:

            #compare list values
            if list1.val < list2.val:

                #make the next pointer for temp be the value from list1
                temp.next = list1
                list1 = list1.next  #move one node over

            else:
                temp.next = list2
                list2 = list2.next
            
            #move temp one node over to be able to add new nodes
            temp = temp.next

        #if there still items in list 1, add them 
        if list1:
            temp.next = list1

        #if there still items in list 2, add them 
        if list2:
            temp.next = list2

        #return the new list at the next pointer where the linked list actually beings, skipping the dummy node
        return new_list.next
    
    #This implementation will use two pointers which will avoid the need of extra memory
    #Time complexity O(n)
    #Space complexity O(1)
    def hasCycle(self, head):
        if head is None:
            return False

        #use two pointers
        slow, fast = head,head

        #traverse and exit the loop based on the fast pointer
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next

            #check if the slow and fast pointer is the same node
            if slow == fast:
                return True

        return False

    #This implementation for checking if there is a cycle will use a set, which will increase memory usage
    #Time complexity O(n)
    #Space complexity O(n)
    def hasCycle2(self, head):
        visited = set()

        while head:
            if head not in visited:
                visited.add(head)
                head = head.next
            else:
                return True
        return False