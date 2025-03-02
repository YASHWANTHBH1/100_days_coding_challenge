# LeetCode Problem Number: 1588
# Problem Link: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        Calculates the sum of all odd-length subarrays.
        
        :param arr: List[int] - Input array.
        :return: int - Sum of all odd-length subarrays.
        """
        total = sum(arr)  # Start with sum of single elements
        n = len(arr)

        # Iterate over odd lengths (3, 5, 7, ...)
        for length in range(3, n + 1, 2):
            for start in range(n):
                if (start + length) > n:  # Ensure subarray doesn't go out of bounds
                    break
                total += sum(arr[start:start + length])  # Sum current subarray
        
        return total

# Taking user input
input_list = list(map(int, input("Enter numbers (space-separated): ").split()))

solution = Solution()
result = solution.sumOddLengthSubarrays(input_list)

# Printing result
print("\nSum of All Odd Length Subarrays:", result)
#
# Time Complexity: O(n³) - Brute-force approach
# Space Complexity: O(1) - No extra space used