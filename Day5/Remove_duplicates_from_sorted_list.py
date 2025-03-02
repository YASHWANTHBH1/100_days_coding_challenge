#leetcode: 83. Remove Duplicates from Sorted List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next  # Skip duplicate
            cur = cur.next  # Move to the next node
        return head

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)))

# Taking user input
input_str = input("Enter sorted linked list values (space-separated): ")
arr = list(map(int, input_str.split()))

# Creating linked list
head = create_linked_list(arr)

# Displaying the original list
print("\nBefore removing duplicates:")
print_linked_list(head)

# Removing duplicates
solution = Solution()
new_head = solution.deleteDuplicates(head)

# Displaying the modified list
print("\nAfter removing duplicates:")
print_linked_list(new_head)
# Time complexity: O(n)
# Space Complexity : O(1)