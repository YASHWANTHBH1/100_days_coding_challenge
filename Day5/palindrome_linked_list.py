# LeetCode Problem Number: 234
# Problem Link: https://leetcode.com/problems/palindrome-linked-list/

class ListNode:
    """ Class representing a node in a singly linked list. """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        """
        Checks if a linked list is a palindrome.
        
        :param head: ListNode, the head of the linked list
        :return: bool, True if the list is a palindrome, otherwise False
        """
        if not head or not head.next:
            return True  # An empty list or single-node list is always a palindrome

        # Step 1: Find the middle using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next  # Slow moves one step, Fast moves two

        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev  # Reverse pointer
            prev = slow  # Move prev forward
            slow = tmp  # Move slow forward
        
        # Step 3: Compare the first and reversed second half
        left, right = head, prev  # Right points to reversed half
        while right:  # Only compare second half (right)
            if left.val != right.val:
                return False  # Not a palindrome
            left = left.next
            right = right.next
        
        return True  # It's a palindrome!

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

# Taking user input to create a linked list
input_list = input("Enter a linked list (space-separated values): ")

# Convert input string into integer list and then linked list
head = create_linked_list(list(map(int, input_list.split())))

# Check if the linked list is a palindrome
solution = Solution()
result = solution.isPalindrome(head)

# Print the result
print("\nIs the linked list a palindrome? :", result)

# Time Complexity: O(n) - We traverse the list twice.
# Space Complexity: O(1) - We only use pointers.