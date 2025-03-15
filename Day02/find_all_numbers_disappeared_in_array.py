#leetcode 448. Find All Numbers Disappeared in an Array
#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution(object):
    def findDisappearedNumbers(self, nums):
        missing = []
        
        # Mark the positions by negating values
        for i in nums:
            pos = abs(i) - 1  # Convert value to index
            if nums[pos] > 0:
                nums[pos] *= -1
        
        # Find missing numbers (indices where values are still positive)
        for i in range(len(nums)):
            if nums[i] > 0:
                missing.append(i + 1)#convert index to value
        
        return missing
nums = list(map(int, input("Enter numbers separated by space (1 to n): ").split()))

# Creating an instance of Solution class
solution = Solution()

# Calling findDisappearedNumbers function
missing_numbers = solution.findDisappearedNumbers(nums)

# Printing the missing numbers
print("Missing numbers:", missing_numbers)
# Time complexity: O(n)
# Space complexity: O(1) excluding the output list
