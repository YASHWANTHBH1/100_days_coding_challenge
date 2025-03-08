#leetcode : 1002
#
class Solution(object):
    def commonChars(self, words):
        common = list(words[0])  # Start with first word's characters
        for word in words[1:]:
            new_common = []
            for char in common:  # Iterate over common characters
                if char in word:
                    new_common.append(char)
                    word = word.replace(char, "", 1)  # Remove one occurrence
            common = new_common  # Update the common characters
        return common

# Example Usage:
solution = Solution()
words = ["bella", "label", "roller"]
print(solution.commonChars(words))  # Output: ['e', 'l', 'l']
