#leet code: https://leetcode.com/problems/power-of-two/
#leet code: 231. Power of Two
#Given an integer n, return true if it is a power of two. Otherwise, return false.  An integer n is a power of two, if there exists an integer x such that n == 2^x.

class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0#return true if n is greater than 0 and n & (n - 1) is 0
# Time complexity: O(1)
# Space complexity: O(1)
# Taking input from user
n = int(input("Enter a number: "))