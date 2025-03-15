#leetcode 119. Pascal's Triangle II
# Problem: Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.
#link: https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex):
        """
        Returns the specific row of Pascal's Triangle.

        :param rowIndex: int - The row index (0-based) of Pascal's Triangle.
        :return: List[int] - The requested row as a list.
        """

        # Initialize the row with all elements as 1
        row = [1] * (rowIndex + 1)

        # `up` represents the decreasing numerator in nCr calculation
        up = rowIndex
        # `down` represents the increasing denominator in nCr calculation
        down = 1

        # Compute Pascal's Triangle row using combination formula
        for i in range(1, rowIndex):
            row[i] = row[i - 1] * up // down  # Use integer division for precision
            up -= 1  # Decrease the numerator
            down += 1  # Increase the denominator

        return row


# Taking input from the keyboard
if __name__ == "__main__":
    row_index = int(input("Enter the row index of Pascal's Triangle: "))  # User input
    solution = Solution()
    print(solution.getRow(row_index))  # Print the Pascal's Triangle row
# Time complexity: O(n) - We iterate over each element in the row.
# Space complexity: O(n) - The entire row is stored in memory.