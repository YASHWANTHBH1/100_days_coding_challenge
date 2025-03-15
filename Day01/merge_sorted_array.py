#leetcode: 88
#leetCode link: https://leetcode.com/problems/merge-sorted-array/
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2  # nums 1 with nums2 elements
        nums1.sort()       # Sorting the merged array

# Taking input from user
nums1 = list(map(int, input("Enter the first sorted array (with extra zeros): ").split()))
m = int(input("Enter the number of actual elements in nums1: "))

nums2 = list(map(int, input("Enter the second sorted array: ").split()))
n = int(input("Enter the number of elements in nums2: "))

# Creating an instance of Solution class
solution = Solution()#

# Merging nums2 into nums1
solution.merge(nums1, m, nums2, n)

# Printing the merged sorted array
print("Merged Sorted Array:", nums1)
# Time complexity: O((m+n)log(m+n))
# Space complexity: O(1)