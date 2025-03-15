# leetcode: 169. Majority Element
# https://leetcode.com/problems/majority-element/
class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:#if the count is zero then the candidate is the current number
                candidate = num#assign the current number to the candidate
            count += (1 if num == candidate else -1)#if the current number is the candidate then increment the count else decrement the count
        return candidate#return the candidate
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Creating an instance of Solution class
solution = Solution()

# Calling majorityElement function and printing result
print("Majority Element:", solution.majorityElement(nums))
#time complexity:O(n)
#space complexity:O(1)
