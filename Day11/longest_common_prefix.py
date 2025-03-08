#leetCode link: https://leetcode.com/problems/longest-common-prefix/
#leetcode: 14
class Solution(object):
    def longestCommonPrefix(self, strs):
        # If the list is empty, return an empty string
        if not strs:
            return ""

        # Initialize the result string to store the common prefix
        res = ""

        # Iterate through each character index of the first string
        for i in range(len(strs[0])):
            # Check each string in the list
            for s in strs:
                # If we reach the end of a string or characters don’t match, return result
                if i == len(s) or s[i] != strs[0][i]:
                    return res

            # If the character is common in all strings, add it to the result
            res += strs[0][i]

        # Return the common prefix after checking all possible characters
        return res

# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
# Time Complexity: O(n * m) where n is the number of strings and m is the length of the longest string
# Space Complexity: O(1) excluding the output variable