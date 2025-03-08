#leetcode link:https://leetcode.com/problems/binary-tree-preorder-traversal/
#leetcode:144
class Solution(object):
    def preorderTraversal(self, root):
        # Initialize current node as root and an empty stack
        cur, stack = root, []
        res = []  # List to store preorder traversal result
        
        # Iterate until all nodes are visited
        while cur or stack:
            if cur:
                res.append(cur.val)  # Process the current node (Root)
                stack.append(cur.right)  # Push the right child to stack
                cur = cur.left  # Move to the left child (processed next)
            else:
                cur = stack.pop()  # Backtrack to the right child when left is exhausted
        
        return res  # Return the final preorder traversal list
# Creating Tree: [1, None, 2, 3]
#time complexity:O(n)
#space complexity:O(n)