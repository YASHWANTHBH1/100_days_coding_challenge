# Link: https://leetcode.com/problems/roman-to-integer/
# LeetCode: 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to store Roman numeral values
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, 
                 "C": 100, "D": 500, "M": 1000}
        
        res = 0  # Result variable to store the integer value

        for i in range(len(s)):
            # If the current numeral is smaller than the next one, subtract it
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        
        return res

# 🏆 Example Test Cases (Runnable in VS Code)
if __name__ == "__main__":
    sol = Solution()

    # Test cases
    test_cases = ["III", "LVIII", "MCMXCIV", "XIV", "CDXLIV"]
    
    for roman_numeral in test_cases:
        print(f"romanToInt('{roman_numeral}') → {sol.romanToInt(roman_numeral)}")
# Time Complexity: O(n)
# Space Complexity: O(1)