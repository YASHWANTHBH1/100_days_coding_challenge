# LeetCode Problem Number: 160
# Problem Link: https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode(object):
    """ Definition for singly-linked list. """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        Finds the intersection node of two linked lists.
        
        :param headA: ListNode - Head of the first linked list.
        :param headB: ListNode - Head of the second linked list.
        :return: ListNode or None - The intersection node, or None if no intersection exists.
        """
        l1, l2 = headA, headB

        while l1 != l2:
            # Move to next node, or switch to the other list's head if at the end
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1  # This is the intersection node or None

# Utility function to create a linked list from a list of values
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Utility function to print a linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Creating test cases
listA = create_linked_list([4, 1, 8, 4, 5])
listB = create_linked_list([5, 6, 1])

# Manually setting intersection at node with value 8
intersect_node = listA.next.next  # Node with value 8
listB.next.next.next = intersect_node  # Connecting listB to listA at intersection

solution = Solution()
intersection = solution.getIntersectionNode(listA, listB)

# Printing result
if intersection:
    print("\nIntersection Node Value:", intersection.val)
else:
    print("\nNo Intersection")
# Time Complexity: O(m + n)
# Space Complexity: O(1)