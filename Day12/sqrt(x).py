#leetcode: https://leetcode.com/problems/sqrtx/
#leet code: 69. Sqrt(x)
class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x  # Handle base cases
        
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid  # Exact square root
            elif mid * mid < x:
                left = mid + 1
                ans = mid  # Store the last valid integer sqrt
            else:
                right = mid - 1
        
        return ans  # Return the integer part of sqrt(x)
# Taking input from user 
x = int(input("Enter a number: "))
# Creating an instance of Solution class