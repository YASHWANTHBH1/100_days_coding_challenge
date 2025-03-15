#leetcode: 977. Squares of a Sorted Array
#https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution(object):
    def sortedSquares(self, nums):
        l = 0
        r = len(nums) - 1
        result = [0] * len(nums)
        k = len(nums) - 1
        while l <= r:
            left_sq = nums[l] ** 2
            right_sq = nums[r] ** 2
            if left_sq > right_sq:
                result[k] = left_sq
                l += 1
            else:
                result[k] = right_sq
                r -= 1
            k -= 1
        return result

# Taking input from user
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Creating an instance of Solution class
solution = Solution()

# Calling sortedSquares function and printing result
print("Sorted Squares:", solution.sortedSquares(nums))
# Time complexity: O(n)
# Space complexity: O(n)
