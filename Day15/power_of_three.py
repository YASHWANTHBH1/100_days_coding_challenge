# Link: https://leetcode.com/problems/power-of-three/
# Problem: Given an integer n, return true if it is a power of three. Otherwise, return false.
#leetcode 326. Power of Three
import math

class Solution:
    def isPowerOfThree(self, n):
        """
        Checks if a number is a power of three.

        :param n: int - The input number.
        :return: bool - True if n is a power of three, else False.
        """
        return n > 0 and (math.log10(n) / math.log10(3)) % 1 == 0


# Taking input from the keyboard
if __name__ == "__main__":
    n = int(input("Enter a number: "))  # User input
    solution = Solution()
    
    # Checking if the number is a power of three
    result = solution.isPowerOfThree(n)
    
    # Printing the result
    print(f"Is {n} a power of three? {result}")
# Time complexity: O(1) - The function runs in constant time.
# Space complexity: O(1) - The function uses a constant amount of space.