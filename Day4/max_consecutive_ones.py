# LeetCode Problem Number: 485
# Problem Link: https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        Finds the maximum number of consecutive 1s in a binary array.
        
        :param nums: List[int] - The input binary array
        :return: int - Maximum consecutive 1s count
        """
        con_count = 0  # Counter for current consecutive 1s
        max_count = 0  # Maximum consecutive 1s found

        for num in nums:
            if num == 1:
                con_count += 1  # Increase count if it's a 1
                max_count = max(max_count, con_count)  # Update max count
            else:
                con_count = 0  # Reset count if it's a 0
        
        return max_count  # Return the maximum count of consecutive 1s

# Taking user input to create a binary list
input_list = input("Enter a binary list (space-separated values): ")

# Convert input string into integer list
nums = list(map(int, input_list.split()))

# Call the function
solution = Solution()
result = solution.findMaxConsecutiveOnes(nums)

# Print the result
print("\nMaximum Consecutive 1s:", result)
# 
# Time Complexity: O(n) - We traverse the array once.
# Space Complexity: O(1) - We use only integer variables.
