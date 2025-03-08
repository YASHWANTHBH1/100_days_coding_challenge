#leetCode: 28. Implement strStr()
#leetCode link: https://leetcode.com/problems/implement-strstr/
class Solution(object):
    def strStr(self, haystack, needle):
        # Edge case: If needle is an empty string, return 0 (as per problem statement)
        if needle == "":
            return 0

        # Iterate through haystack, stopping at positions where the remaining substring is at least as long as needle
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring of haystack starting at index `i` matches `needle`
            if haystack[i: i + len(needle)] == needle:
                return i  # Found match, return index

        # If no match is found, return -1
        return -1

# Example usage:
solution = Solution()
print(solution.strStr("hello", "ll"))  # Output: 2
print(solution.strStr("aaaaa", "bba"))  # Output: -1
print(solution.strStr("", ""))  # Output: 0
# Time Complexity: O(n * m) where n is the length of haystack and m is the length of needle
# Space Complexity: O(1) excluding the output variable
