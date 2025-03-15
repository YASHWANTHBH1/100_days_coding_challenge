# LeetCode Problem Number: 844
# Problem Link: https://leetcode.com/problems/backspace-string-compare/

class Solution(object):
    def backspaceCompare(self, s, t):
        """Compares two strings as if '#' acts as a backspace."""
        
        # Helper function to find next valid character
        def nextValidChar(string, index):
            backspace = 0
            while index >= 0:
                if string[index] == "#":
                    backspace += 1  # Count backspace
                elif backspace > 0:
                    backspace -= 1  # Ignore character
                else:
                    break  # Found a valid character
                index -= 1
            return index  # Return index of valid character
        
        # Initialize pointers
        index_s, index_t = len(s) - 1, len(t) - 1

        # Compare characters from end to start
        while index_s >= 0 or index_t >= 0:
            index_s = nextValidChar(s, index_s)
            index_t = nextValidChar(t, index_t)
            
            # Get actual characters (or empty string if index < 0)
            char_s = s[index_s] if index_s >= 0 else ""
            char_t = t[index_t] if index_t >= 0 else ""
        
            # If the characters are different, return False
            if char_s != char_t:
                return False
            
            # Move both pointers to the left
            index_s -= 1
            index_t -= 1
        
        return True  # Strings match after processing backspaces

# Test Cases
sol = Solution()
print(sol.backspaceCompare("ab#c", "ad#c"))  # True (both -> "ac")
print(sol.backspaceCompare("ab##", "c#d#"))  # True (both -> "")
print(sol.backspaceCompare("a#c", "b"))      # False ("c" != "b")
print(sol.backspaceCompare("xywrrmp", "xywrrmu#p"))  # True
#
# Time Complexity: O(n + m)
# Space Complexity: O(1)
