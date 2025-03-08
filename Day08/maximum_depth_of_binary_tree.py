#leetcode: 104. Maximum Depth of Binary Tree - Easy
#https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        Function to find the maximum depth of a binary tree.
        :type root: TreeNode
        :rtype: int
        """
        # If the tree is empty, return 0
        if not root:
            return 0
        
        # Recursively calculate the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # The maximum depth is the greater of left or right depth + 1 (for current node)
        return 1 + max(left_depth, right_depth)
    #time complexity: O(n)
    #space complexity: O(n)
