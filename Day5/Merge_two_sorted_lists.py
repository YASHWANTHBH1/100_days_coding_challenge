# LeetCode Problem Number: 21
# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    """ Class representing a node in a singly linked list. """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        Merges two sorted linked lists into one sorted linked list.

        :param list1: ListNode, the head of the first sorted linked list
        :param list2: ListNode, the head of the second sorted linked list
        :return: ListNode, the head of the merged sorted linked list
        """
        # Dummy node to track the start of the merged list
        dummy = ListNode()
        tail = dummy  # Tail pointer to track the last node in the merged list

        # Iterate while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:  # Choose the smaller value
                tail.next = list1       # Attach list1 node to merged list
                list1 = list1.next      # Move list1 pointer forward
            else:
                tail.next = list2       # Attach list2 node to merged list
                list2 = list2.next      # Move list2 pointer forward
            
            tail = tail.next  # Move the tail pointer forward

        # If any nodes are left in either list, attach them
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next  # Return the merged list starting from dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(arr):
    """
    Converts a Python list into a linked list.

    :param arr: List of integers
    :return: Head node of the linked list
    """
    if not arr:
        return None  # Return None if the input list is empty
    head = ListNode(arr[0])  # Create the head node
    cur = head
    for val in arr[1:]:  # Iterate through remaining values
        cur.next = ListNode(val)  # Create and link new node
        cur = cur.next  # Move current pointer forward
    return head  # Return the head of the linked list

# Helper function to print a linked list
def print_linked_list(head):
    """
    Prints the linked list in a readable format.

    :param head: Head node of the linked list
    """
    values = []
    while head:  # Traverse the linked list
        values.append(head.val)  # Store node values
        head = head.next
    print(" -> ".join(map(str, values)) if values else "Empty List")

# Taking user input to create two sorted linked lists
input1 = input("Enter sorted list1 (space-separated): ")
input2 = input("Enter sorted list2 (space-separated): ")

# Convert input strings into integer lists and then linked lists
list1 = create_linked_list(list(map(int, input1.split())))
list2 = create_linked_list(list(map(int, input2.split())))

# Display the original lists
print("\nList 1:")
print_linked_list(list1)
print("\nList 2:")
print_linked_list(list2)

# Merge the two sorted linked lists
solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

# Display the merged sorted linked list
print("\nMerged Sorted List:")
print_linked_list(merged_head)

# Time Complexity: O(n + m) where n and m are the lengths of the two lists.
# Space Complexity: O(1) since we modify the existing lists without extra space.
