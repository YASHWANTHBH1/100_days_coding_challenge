#leetCode: 206. Reverse Linked List
# Reverse a singly linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next  # Swapping in one line
        return prev

# Helper function to create a linked list from user input
def create_linked_list(values):
    head = ListNode(values[0]) if values else None
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

# Taking input from user
values = list(map(int, input("Enter linked list elements (comma-separated): ").split(',')))

# Creating and printing original linked list
head = create_linked_list(values)
print("Original Linked List:")
print_linked_list(head)

# Reversing and printing the reversed linked list
solution = Solution()
reversed_head = solution.reverseList(head)
print("Reversed Linked List:")
print_linked_list(reversed_head)
# Time complexity: O(n)
# Space complexity: O(1)
