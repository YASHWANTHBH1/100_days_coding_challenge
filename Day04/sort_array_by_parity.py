# LeetCode Problem Number: 905
# Problem Link: https://leetcode.com/problems/sort-array-by-parity/

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        Sorts an array by placing even numbers first, then odd numbers.
        
        :param nums: List[int] - Input array.
        :return: List[int] - Sorted array with evens first.
        """
        left, right = 0, len(nums) - 1  # Two-pointer approach
        while left < right:
            # Swap if left is odd and right is even
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]

            # Move left pointer forward if it's even
            if nums[left] % 2 == 0:
                left += 1

            # Move right pointer backward if it's odd
            if nums[right] % 2 == 1:
                right -= 1
        
        return nums

# Taking user input
input_list = list(map(int, input("Enter numbers (space-separated): ").split()))

solution = Solution()
sorted_array = solution.sortArrayByParity(input_list)

# Printing sorted array
print("\nSorted Array by Parity:", sorted_array)
# Time Complexity: O(n) - Iterates through the list once
# Space Complexity: O(1) - Modifies the list in-place