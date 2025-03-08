#leetcode 58. Length of Last Word
#https://leetcode.com/problems/length-of-last-word/
def length_of_last_word(s):
    # Strip leading and trailing spaces to handle cases like "   Hello World   "
    s = s.strip()

    # Split the string into a list of words using whitespace as a delimiter
    words = s.split()

    # Return the length of the last word if words exist, otherwise return 0
    return len(words[-1]) if words else 0

# Example usage:
s = "Hello World"
print(length_of_last_word(s))  # Output: 5

s2 = "   Python is fun  "
print(length_of_last_word(s2))  # Output: 3 (fun)
# Time complexity: O(n)
# Space complexity: O(n) excluding the output variable
