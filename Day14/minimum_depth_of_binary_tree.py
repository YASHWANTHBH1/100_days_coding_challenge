# Problem: Minimum Depth of Binary Tree
# Problem Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/`
# Given a binary tree, find its minimum depth.
# leetcode: 111. Minimum Depth of Binary Tree`
class Solution(object):
    def minDepth(self, root):
        if root ==None:
            return 0
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1
# Taking input from user
root = [3,9,20,None,None,15,7]  
# Creating an instance of Solution class
solution = Solution()
# Calling minDepth function and printing result
print("Minimum Depth of Binary Tree:", solution.minDepth(root))