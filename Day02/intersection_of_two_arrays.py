#leet code: 349. Intersection of Two Arrays
#https://leetcode.com/problems/intersection-of-two-arrays/
class Solution(object):
    def intersection(self, nums1, nums2):#function to find the intersection of two arrays
        set1 = set(nums1)#convert the first list to a set
        set2 = set(nums2)#convert the second list to a set
        return list(set1 & set2)  # Set intersection

nums1 = list(map(int, input("Enter numbers for the first list separated by space: ").split()))
nums2 = list(map(int, input("Enter numbers for the second list separated by space: ").split()))

# Creating an instance of Solution class
solution = Solution()

# Calling intersection function
result = solution.intersection(nums1, nums2)

# Printing the intersection of both lists
print("Intersection of both lists:", result)
# Time complexity: O(n)
# Space complexity: O(n)
