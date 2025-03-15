# LeetCode: 1480
# https://leetcode.com/problems/running-sum-of-1d-array/
# Given an array nums, return the running sum of nums where runningSum[i] = sum(nums[0]...nums[i]).

class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):  # Iterate through the list from index 1
            nums[i] += nums[i - 1]  # Add previous sum to current element
        return nums  

# Taking user input as a list of integers
nums = list(map(int, input("Enter numbers separated by space: ").split()))

solution = Solution()
result = solution.runningSum(nums)
print(result)

# Time Complexity: O(n)
# Space Complexity: O(1)
