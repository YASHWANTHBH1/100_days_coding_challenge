#leetcode : 145. Binary Tree Postorder Traversal
#https://leetcode.com/problems/binary-tree-postorder-traversal/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        
        stack = [root]
        visit = [False]
        res = []
        
        while stack:
            cur, v = stack.pop(), visit.pop()
            if cur:
                if v:
                    res.append(cur.val)  # Process node
                else:
                    stack.append(cur)  # Push current node back for processing later
                    visit.append(True)  # Mark for future processing
                    
                    if cur.right:  # Push right child
                        stack.append(cur.right)
                        visit.append(False)
                    
                    if cur.left:  # Push left child
                        stack.append(cur.left)
                        visit.append(False)

        return res

# Creating Tree: [1, None, 2, 3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
print(sol.postorderTraversal(root))  # Expected Output: [3, 2, 1]
# Time Complexity: O(n)
# Space Complexity: O(n)
