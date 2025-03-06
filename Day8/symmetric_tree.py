#leetcode: 101. Symmetric Tree
#https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        Checks if a binary tree is symmetric (mirror of itself).
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(left, right):
            if not left and not right:  # Both nodes are None
                return True
            if not left or not right:  # One node is None while the other isn't
                return False
            return (left.val == right.val and 
                    dfs(left.left, right.right) and 
                    dfs(left.right, right.left))

        if not root:  # An empty tree is symmetric
            return True
        
        return dfs(root.left, root.right)
    #time complexity: O(n)
    #space complexity: O(n)