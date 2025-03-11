# leetcode: https://leetcode.com/problems/add-binary/
# LeetCode: 67. Add Binary
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
# Taking input from user
a = input("Enter binary number a: ") 