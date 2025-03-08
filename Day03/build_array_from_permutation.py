# LeetCode: 1920
# https://leetcode.com/problems/build-array-from-permutation/
# Given an array nums, build an array ans where ans[i] = nums[nums[i]] and return ans.

class Solution:
    def buildArray(self, nums):
        ans = [nums[nums[i]] for i in range(len(nums))]  # Constructing the permutation array
        return ans

# User input
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Solution instance
solution = Solution()
result = solution.buildArray(nums)

# Output result
print("Output:", result)

# Time Complexity: O(n)
# Space Complexity: O(n)
