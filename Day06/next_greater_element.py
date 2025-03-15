# LeetCode Problem Number: 496
# Problem Link: https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        Finds the next greater element for each element in nums1 within nums2.

        :param nums1: List[int] - Query list
        :param nums2: List[int] - Main list
        :return: List[int] - List of next greater elements (or -1 if none exists)
        """
        # Store indices of nums1 elements in nums2
        nums1Indx = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)  # Default -1 for each element
        stack = []  # Monotonic decreasing stack

        # Iterate over nums2
        for cur in nums2:
            # Process the stack
            while stack and cur > stack[-1]:  
                val = stack.pop()  # Find next greater element for this value
                idx = nums1Indx[val]
                res[idx] = cur  # Update result array

            # Push element to stack if it's in nums1
            if cur in nums1Indx:
                stack.append(cur)

        return res

# Test Cases
solution = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print("\nNext Greater Elements (Expected: [-1, 3, -1]):", solution.nextGreaterElement(nums1, nums2))

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print("Next Greater Elements (Expected: [3, -1]):", solution.nextGreaterElement(nums1, nums2))
#
# Time Complexity: O(n + m)
# Space Complexity: O(n)