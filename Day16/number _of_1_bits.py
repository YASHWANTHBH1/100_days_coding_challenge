# This is a solution to the problem of counting the number of 1 bits in the binary representation of an unsigned integer.
# Link: https://leetcode.com/problems/number-of-1-bits/
#leetcode 191. Number of 1 Bits
class Solution:
    def hammingWeight(self, n):
        """
        Counts the number of 1 bits in the binary representation of n.

        :param n: int - An unsigned integer.
        :return: int - The number of 1 bits in its binary form.
        """
        count = 0  # Counter for the number of 1s
        while n != 0:
            if n & 1 == 1:  # Check if the last bit is 1
                count += 1
            n = n >> 1  # Right shift n by 1 bit
        return count


# Taking input from the keyboard
if __name__ == "__main__":
    n = int(input("Enter a number: "), 2)  # User inputs a binary number (e.g., "00000000000000000000000000001011")
    solution = Solution()
    
    # Counting the number of 1 bits
    result = solution.hammingWeight(n)
    
    # Printing the result
    print(f"Number of 1 bits: {result}")
# Time complexity: O(1) - The function runs in constant time.
# Space complexity: O(1) - The function uses a constant amount of space.