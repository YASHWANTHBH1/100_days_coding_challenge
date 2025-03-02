# LeetCode Problem Number: 876
# Problem Link: https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode:
    """ Class representing a node in a singly linked list. """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        """
        Finds the middle node of a singly linked list.
        
        :param head: ListNode, the head of the linked list
        :return: ListNode, the middle node of the linked list
        """
        slow, fast = head, head  # Initialize slow and fast pointers
        
        # Move fast by 2 steps and slow by 1 step until fast reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow  # Slow is now at the middle node

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

# Taking user input to create a linked list
input_list = input("Enter a linked list (space-separated values): ")

# Convert input string into integer list and then linked list
head = create_linked_list(list(map(int, input_list.split())))

# Display the original linked list
print("\nOriginal Linked List:")
print_linked_list(head)

# Find the middle node
solution = Solution()
middle = solution.middleNode(head)

# Display the middle node and the remaining list from the middle
print("\nMiddle Node and Remaining List:")
print_linked_list(middle)
# Time Complexity: O(n) - We traverse the list once.
# Space Complexity: O(1) - We only use two pointers.