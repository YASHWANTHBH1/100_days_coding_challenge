#leetcode link: https://leetcode.com/problems/remove-element/
#leetcode: 27
class Solution(object):
    def removeElement(self, nums, val):
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]#swapping the vale if i with j means swapping val with other numbers
                j += 1
        return j

# Taking input from the user
nums = list(map(int, input("Enter the numbers separated by space: ").split()))
val = int(input("Enter the value to remove: "))

# Creating an instance of Solution class
solution = Solution()

# Calling removeElement function
new_length = solution.removeElement(nums, val)

# Printing the result
print("New length after removal:", new_length)
print("Updated list:", nums[:new_length])
# Time complexity: O(n)
# Space complexity: O(1) excluding the output variable