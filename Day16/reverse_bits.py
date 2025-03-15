#leetcode 190. Reverse Bits
# Problem: Reverse bits of a given 32 bits unsigned integer.    
# Link: https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n):
        """
        Reverses the bits of a given 32-bit unsigned integer.

        :param n: int - An unsigned integer.
        :return: int - The reversed bits as an integer.
        """
        res = 0  # Initialize the result
        for i in range(32):  # Iterate over all 32 bits
            res = res << 1  # Shift result left
            res += (n & 1)  # Get the last bit of n and add it to res
            n = n >> 1  # Right shift n to process the next bit
        return res


# Taking input from the keyboard
if __name__ == "__main__":
    n = int(input("Enter a 32-bit integer: "))  # User input as an integer
    solution = Solution()
    
    # Reversing the bits
    result = solution.reverseBits(n)
    
    # Printing the result
    print(f"Reversed bits integer: {result}")
# Time complexity: O(1) - The function runs in constant time.
# Space complexity: O(1) - The function uses a constant amount of space.