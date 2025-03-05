# LeetCode 226: Invert Binary Tree
# Problem Statement:
# Given the root of a binary tree, invert the tree and return its root.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node value
        self.left = left  # Left subtree
        self.right = right  # Right subtree

class Solution(object):
    def invertTree(self, root):
        # Base case: If root is None, return None
        if not root:
            return None
        
        # Swap left and right subtrees
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        # Return the root after inverting
        return root

# Helper function to print tree in level order
from collections import deque

def level_order(root):
    if not root:
        return []  # Return empty if root is None
    queue = deque([root])  # Use a queue for BFS
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val if node else None)  # Add node value to result
        if node:
            queue.append(node.left)
            queue.append(node.right)
    return result  # Return list representation of the tree

root = TreeNode(4,
                TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(7, TreeNode(6), TreeNode(9)))

# Print original tree
print("Original Tree:", level_order(root))

# Call the invertTree function
solution = Solution()
inverted_root = solution.invertTree(root)

# Print inverted tree
print("Inverted Tree:", level_order(inverted_root))
