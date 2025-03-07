# Link: https://leetcode.com/problems/valid-anagram/
# LeetCode: 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Sort both strings and compare them
        return sorted(s) == sorted(t)

# 🏆 Example Test Cases (Runnable in VS Code)
if __name__ == "__main__":
    sol = Solution()

    # Test cases
    test_cases = [
        ("listen", "silent"),  # True - valid anagram
        ("rat", "car"),        # False - different letters
        ("aacc", "ccac"),      # False - different frequency
        ("anagram", "nagaram") # True - valid anagram
    ]

    for s, t in test_cases:
        print(f"isAnagram('{s}', '{t}') → {sol.isAnagram(s, t)}")
# Time Complexity: O(n log n)
# Space Complexity: O(n)
