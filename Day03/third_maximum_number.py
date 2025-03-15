# LeetCode: 414
# https://leetcode.com/problems/third-maximum-number/
# Given an integer array nums, return the third distinct maximum number in this array. 
# If the third maximum does not exist, return the maximum number.

class Solution(object):
    def thirdMax(self, nums):
        num_set = set(nums)  # Convert list to set to remove duplicates
        nums = sorted(num_set, reverse=True)  # Sort in descending order
        
        if len(nums) >= 3:  # If there are at least 3 distinct elements
            return nums[2]  # Return the third maximum
        return nums[0]  # Otherwise, return the maximum
        
# Taking user input as a list of integers
nums = list(map(int, input("Enter numbers separated by space: ").split()))

solution = Solution()
result = solution.thirdMax(nums)
print(result)

# Time Complexity: O(n log n)
# Space Complexity: O(n)
