# leetcode: 20
#leetcode link: https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        stack = []#stack to store the opening brackets
        matching_brackets = {')': '(', '}': '{', ']': '['}#dictionary to store the matching brackets
        
        for char in s:
            if char in matching_brackets.values():#if the character is an opening bracket
                stack.append(char)#append it to the stack
            elif char in matching_brackets:#if the character is a closing bracket
                if stack and stack[-1] == matching_brackets[char]:#if the stack is not empty and the last element in the stack is the matching opening bracket
                    stack.pop()#pop the last element from the stack
                else:
                    return False
        return not stack#return true if the stack is empty else return false

s = input("Enter a string of parentheses: ")
solution = Solution()

# Calling isValid function and printing result
print("Is the string valid?:", solution.isValid(s))
# Time complexity: O(n)
# Space complexity: O(n)
