'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
Example 1:
  Input: 1->1->2
  Output: 1->2
Example 2:
  Input: 1->1->2->3->3
  Output: 1->2->3
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # Check for empty SLL
        if head == None:
            return head
        
        # Move from head to the next node
        currentNode = head.next
        # Set a previous node to head at first and update as you go through SLL
        prevNode = head
        # Loop through SLL
        while currentNode != None:
            # Not a duplicate value
            # Check current value to previous node's value
            if currentNode.val != prevNode.val:
                # Update the previous node to point to current node
                prevNode = currentNode
                # Just move forward
                currentNode = currentNode.next
            # Duplicate value found
            else:
                #print("duplicate found")
                # Remove from linked list by assigning the next node to previous node
                prevNode.next = currentNode.next
                # Jump to that next node
                currentNode = currentNode.next

        return head
