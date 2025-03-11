# Link: https://leetcode.com/problems/plus-one/
# LeetCode: 66. Plus One
class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        
        # Start adding from the last digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # If it's 9, turn it to 0 and continue
        
        # If all digits were 9, we need an extra digit at the front
        return [1] + digits