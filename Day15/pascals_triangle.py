# This program generates Pascal's Triangle up to the given number of rows.
#leetcode 118. Pascal's Triangle
# Problem: Given an integer numRows, return the first numRows of Pascal's triangle.
#link: https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows):
        """
        Generates Pascal's Triangle up to the given number of rows.

        :param numRows: int - Number of rows in Pascal's Triangle.
        :return: List[List[int]] - Pascal's Triangle as a list of lists.
        """

        # Initialize Pascal's Triangle with all 1s
        pascal = [[1] * (i + 1) for i in range(numRows)]

        # Compute values for the inner elements
        for i in range(2, numRows):  # Start from row 2 (index-based)
            for j in range(1, i):  # Ignore the first and last element
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

        return pascal


# Taking input from the keyboard
if __name__ == "__main__":
    numRows = int(input("Enter the number of rows for Pascal's Triangle: "))  # User input
    solution = Solution()
    
    # Generating Pascal's Triangle
    triangle = solution.generate(numRows)
    
    # Printing the result in a readable format
    for row in triangle:
        print(row)
# Time complexity: O(n^2) - We iterate over each element in the triangle.
# Space complexity: O(n^2) - The entire triangle is stored in memory.
