#leetcode: 94. Binary Tree Inorder Traversal
#same input as before
#https://leetcode.com/problems/binary-tree-inorder-traversal/
class Solution(object):
    def inorderTraversal(self, root):
        # Initialize an empty list to store traversal result
        res = []
        
        # Helper function for recursive inorder traversal
        def inorder(root):
            if not root:  # Base case: if the node is None, return
                return
            inorder(root.left)  # Traverse the left subtree
            res.append(root.val)  # Process the current node (root)
            inorder(root.right)  # Traverse the right subtree

        inorder(root)  # Start recursive traversal from the root
        return res  # Return the final inorder traversal list
# Creating Tree: [1, None, 2, 3]
#time complexity:O(n)
#space complexity:O(n)
