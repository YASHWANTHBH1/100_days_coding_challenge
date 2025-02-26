#leetCode link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#leetcode: 26
class Solution(object):
    def removeDuplicates(self, nums):
        l = 1  # Pointer for the unique elements
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:  # Check if the current element is different from the previous one
                nums[l] = nums[r]  # Move unique element forward
                l += 1
        return l

# Taking input from user
nums = list(map(int, input("Enter a sorted list of numbers separated by space: ").split()))

# Creating an instance of Solution class
solution = Solution()

# Calling removeDuplicates function
new_length = solution.removeDuplicates(nums)

# Printing the updated list (only unique elements up to index new_length)
print("List after removing duplicates:", nums[:new_length])
print("New length of the array:", new_length)
# Time complexity: O(n)
#
# Space complexity: O(1)
