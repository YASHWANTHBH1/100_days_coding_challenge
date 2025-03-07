# Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# LeetCode: 108. Convert Sorted Array to Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        # Find the middle element
        mid = len(nums) // 2
        
        # Create the root node with the middle element
        root = TreeNode(val=nums[mid])

        # Recursively construct the left subtree with left half of the array
        root.left = self.sortedArrayToBST(nums[:mid])

        # Recursively construct the right subtree with right half of the array
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root

# Helper function to print tree in Inorder Traversal
def inorderTraversal(root):
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

# 🏆 Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [[-10, -3, 0, 5, 9], [1, 3], [0], []]

    for nums in test_cases:
        tree = sol.sortedArrayToBST(nums)
        print(f"Sorted Array: {nums} → BST Inorder Traversal: {inorderTraversal(tree)}")
# Time Complexity: O(n)
# Space Complexity: O(n)