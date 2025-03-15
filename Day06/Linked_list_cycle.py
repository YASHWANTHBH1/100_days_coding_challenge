# LeetCode Problem Number: 141
# Problem Link: https://leetcode.com/problems/linked-list-cycle/

class ListNode(object):
    """ Definition for singly-linked list. """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        Detects if the linked list has a cycle.

        :param head: ListNode - Head of the linked list.
        :return: bool - True if there is a cycle, False otherwise.
        """
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Cycle detected
                return True
        
        return False  # No cycle

# Utility function to create a linked list from a list of values
def create_linked_list(arr, pos):
    """
    Creates a linked list and introduces a cycle if pos is not -1.

    :param arr: List[int] - Values for the linked list.
    :param pos: int - Position where the cycle should start (-1 for no cycle).
    :return: ListNode - Head of the linked list.
    """
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    cycle_start = None

    for index, val in enumerate(arr[1:], start=1):
        current.next = ListNode(val)
        current = current.next
        if index == pos:  # Mark the cycle start node
            cycle_start = current

    if pos != -1:
        current.next = cycle_start  # Create cycle

    return head

# Test Cases
list_with_cycle = create_linked_list([3, 2, 0, -4], 1)  # Cycle at index 1 (value 2)
list_without_cycle = create_linked_list([1, 2, 3, 4], -1)  # No cycle

solution = Solution()
print("\nHas Cycle (Expected: True):", solution.hasCycle(list_with_cycle))
print("Has Cycle (Expected: False):", solution.hasCycle(list_without_cycle))
# Time Complexity: O(n)
# Space Complexity: O(1)
