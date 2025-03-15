#leetcode: https://leetcode.com/problems/pascals-triangle/
#LeetCode: 118. Pascal's Triangle
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
class Solution(object):
    def generate(self, numRows):
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(2,numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]
        return pascal
# Taking input from user
numRows = int(input("Enter number of rows: "))