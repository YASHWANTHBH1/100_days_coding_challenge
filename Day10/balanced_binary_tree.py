# Link: https://leetcode.com/problems/balanced-binary-tree/
# LeetCode: 110. Balanced Binary Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        def dfs(root):
            if not root:
                return [True, 0]  # (Is balanced, Height of subtree)

            # Recursively check left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # A tree is balanced if:
            # - Left and right subtrees are balanced
            # - The height difference is at most 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # Return [IsBalanced, Height]
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]  # Return only the balanced status

# 🔄 Helper function to build a tree from a list (for easy testing)
def buildTree(nodes, index=0):
    if index >= len(nodes) or nodes[index] is None:
        return None
    root = TreeNode(nodes[index])
    root.left = buildTree(nodes, 2 * index + 1)
    root.right = buildTree(nodes, 2 * index + 2)
    return root

# 🏆 Test Cases
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [3, 9, 20, None, None, 15, 7],  # Balanced Tree
        [1, 2, 2, 3, 3, None, None, 4, 4],  # Unbalanced Tree
        [],  # Empty Tree (Balanced)
        [1]  # Single Node (Balanced)
    ]

    for nodes in test_cases:
        tree = buildTree(nodes)
        print(f"Tree {nodes} → Is Balanced? {sol.isBalanced(tree)}")
# Time Complexity: O(n)
# Space Complexity: O(n) - for the recursive stack
