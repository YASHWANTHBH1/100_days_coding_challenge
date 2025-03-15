# Write a bash script to extract all valid phone numbers from a text file file.txt.
#leetcode: https://leetcode.com/problems/valid-phone-numbers/
#LeetCode: 193. Valid Phone Numbers
import re
with open('file.txt', 'r') as file:
    for line in file:
        if re.match(r'^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$', line.strip()):
            print(line.strip())
# Time complexity: O(n)
# Space complexity: O(1)
# The above code reads the file line by line and uses regular expression to match the valid phone numbers.
# The regular expression ^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$ matches the following patterns:
# 1. (123) 456-7890
# 2. 123-456-7890   (Note: The space after the area code is optional)                                       