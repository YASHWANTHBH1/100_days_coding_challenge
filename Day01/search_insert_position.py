#leetcode 35. Search Insert Position
#https://leetcode.com/problems/search-insert-position/
#here we use binary search to find the index of the target element in the sorted array

class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1#initialize the low and high index
        while low <= high:
            mid = low + (high - low) // 2#calculate the mid index
            if nums[mid] == target:#if the mid element is equal to the target then return the mid index
                return mid
            elif nums[mid] < target:#if the mid element is less than the target then search in the right half
                low = mid + 1
            else:
                high = mid - 1#search in the left half
        return low

nums = list(map(int, input("Enter sorted numbers separated by space: ").split()))
target = int(input("Enter the target number: "))

# Creating an instance of Solution class
solution = Solution()

# Calling searchInsert function and printing result
print("Insert position:", solution.searchInsert(nums, target))
# Time complexity: O(log n)
# Space complexity: O(1)
