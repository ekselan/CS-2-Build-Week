"""
Merge Two Sorted Lists
----------------------

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        # Want to go through each linked list
        # Need to traverse, can start with head node        
        # And put those values into a single array
        # I'll sort that single array
        # And then convert that array into a linked list
            # May need helper methods/functions to 
                # Add to a linked list
                # To convert an array into a linked list
                    # Converting the arr will involve itertating through
                    # And making the first item the head node, and the rest are .nexts in order
        """
        
        def extract_vals(ll, arr):
            """
            Inputs: ll: ListNode (linked list)
                    arr: empty array (to be filled)
            """
            root = ll
            
            # Handle edge case
            if root is None:
                return arr
            
            while root.next:
                # want to store that first value
                arr.append(root.val)
                # set up next node
                root = root.next

            # append last val
            arr.append(root.val)
            
            return arr
        
        l1_vals = []
        l1_vals = extract_vals(l1, l1_vals)
        l2_vals = []
        l2_vals = extract_vals(l2, l2_vals)
        
        # Add the two lists together
        store = sorted(l1_vals + l2_vals)
        
        
        # print("STORE:", store)
        # print(type(store))
            
        
        # At this point, store is a list that holds the expected vals in appropriate order
        
        # Next step is to convert to linked list
        
        # Need function to add vals to a ListNode
        def add_node(root, val):
            new = ListNode(val)
            
            # if ll is empty, add new val to head
            if root is None:
                root = new
            
            # otherwise, set up traversal
            else:
                pointer = root #> start at head node
                # As long as there's a next, keep updating the pointer
                while pointer.next is not None:
                    pointer = pointer.next
                # Once there are no more nexts, add in the new node
                pointer.next = new

            return root
            
#         test_node = ListNode(3)
#         test_node = add_node(test_node, 3)
#         test_node = add_node(test_node, 4)
#         test_node = add_node(test_node, 5)
#         test_node = add_node(test_node, 6)
        
#         test_vals = []
#         test_vals = extract_vals(test_node, test_vals)
#         print("TEST VALS:", test_vals)

        
        # Now have functionality to add nodes to linked list
        # Can incorporate that in function to convert arr to list
        def arr_to_ll(arr, n):
            root = None
            for i in range(0, n):
                root = add_node(root, arr[i])

            return root
        
        n = len(store)
        ll = arr_to_ll(store, n)
        
        return ll