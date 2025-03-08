# LeetCode Problem Number: 303
# Problem Link: https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(object):

    def __init__(self, nums):
        """
        Initializes the NumArray object with a prefix sum array.
        
        :param nums: List[int] - The input array of numbers.
        """
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n  # Running sum
            self.prefix.append(cur)  # Store prefix sum

    def sumRange(self, left, right):
        """
        Returns the sum of elements from index left to right (inclusive).
        
        :param left: int - Start index
        :param right: int - End index
        :return: int - Sum of elements in range
        """
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0  # Handle edge case when left = 0
        return rightSum - leftSum

# Taking user input
input_list = list(map(int, input("Enter numbers (space-separated): ").split()))
numArray = NumArray(input_list)

# Taking range input
left, right = map(int, input("Enter range (left right): ").split())

# Printing the sum in the range
print("\nSum of range:", numArray.sumRange(left, right))
# Tme Complexity: O(n) - Constructing prefix sum array
# Query Complexity: O(1) - Fetching range sum
# Space Complexity: O(n) - Storing prefix sum array