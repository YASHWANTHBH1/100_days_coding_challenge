# Link: https://leetcode.com/problems/path-sum/
# LeetCode: 112. Path Sum
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val==targetSum
        targetSum=targetSum-root.val
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
# Taking input from user
root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
# Creating an instance of Solution class    
solution = Solution()
# Calling hasPathSum function and printing result
print("Has Path Sum:", solution.hasPathSum(root, targetSum))
# Time complexity: O(n)
# Space complexity: O(n)