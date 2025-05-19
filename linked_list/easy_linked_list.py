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