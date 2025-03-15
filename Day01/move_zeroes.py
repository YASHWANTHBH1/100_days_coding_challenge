#leetcode : 283
#https://leetcode.com/problems/move-zeroes/
#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. 
class Solution(object):
    def moveZeroes(self, nums):
        j = 0#first pointer which helps to move the non zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]#swapping the non zero element with the zero element
                j += 1
        return nums#return the array with all the non zero elements in the front and zero elements in the end

nums = list(map(int, input("Enter the numbers separated by space: ").split()))

# Creating an instance of Solution class
solution = Solution()

# Calling moveZeroes function and printing result
print("Output:", solution.moveZeroes(nums))
# Time complexity: O(n)
# Space complexity: O(1)
