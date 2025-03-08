class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initializes a new ListNode.
        :param val: Value of the node
        :param next: Pointer to the next node
        """
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        """
        Removes all elements with value 'val' from the linked list.
        :param head: Head of the linked list (ListNode)
        :param val: Integer value to be removed
        :return: Modified head of the linked list
        """
        # Step 1: Remove all leading nodes that have the target value
        while head and head.val == val:
            head = head.next  # Move head to the next node
        
        # Step 2: If the entire list is removed, return None
        if not head:
            return None

        # Step 3: Iterate through the list and remove nodes with value 'val'
        current = head  # Start from the head
        while current and current.next:
            if current.next.val == val:  # If the next node has the target value
                current.next = current.next.next  # Skip the node with value 'val'
            else:
                current = current.next  # Move to the next node
        
        return head  # Return the updated head of the list

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    """
    Converts a list of values into a linked list.
    :param values: List of integers
    :return: Head of the linked list
    """
    if not values:
        return None  # If input is empty, return None

    head = ListNode(values[0])  # Create the first node
    current = head  # Pointer to track the last node
    for val in values[1:]:
        current.next = ListNode(val)  # Create a new node and link it
        current = current.next  # Move to the new node
    return head  # Return the head of the linked list

# Helper function to print the linked list
def print_linked_list(head):
    """
    Prints the linked list in a readable format.
    :param head: Head of the linked list
    """
    if not head:
        print("Empty List")
        return

    while head:
        print(head.val, end=" -> " if head.next else "\n")  # Print each node
        head = head.next  # Move to the next node

# Step 1: Take user input for linked list elements
values = list(map(int, input("Enter linked list elements (comma-separated): ").split(',')))

# Step 2: Take user input for the value to remove
val_to_remove = int(input("Enter the value to remove: "))

# Step 3: Create and print the original linked list
head = create_linked_list(values)
print("Original Linked List:")
print_linked_list(head)

# Step 4: Remove the target value from the linked list
solution = Solution()
updated_head = solution.removeElements(head, val_to_remove)

# Step 5: Print the modified linked list
print("Linked List After Removal:")
print_linked_list(updated_head)
