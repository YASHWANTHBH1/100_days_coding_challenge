#leetcode: 80. Remove Duplicates from Sorted Array II
#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution(object):
    def removeDuplicates(self, nums):
        l, r = 0, 0  # Two pointers
        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:  # Count occurrences
                r += 1
                count += 1
            for i in range(min(2, count)):  # Allow at most 2 occurrences
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
nums = list(map(int, input("Enter a sorted list of numbers separated by space: ").split()))
solution = Solution()

# Calling removeDuplicates function
new_length = solution.removeDuplicates(nums)

# Printing the updated list (only unique elements up to index new_length)
print("List after removing duplicates:", nums[:new_length])
print("New length of the array:", new_length)
# Time complexity: O(n)
# Space complexity: O(1)
