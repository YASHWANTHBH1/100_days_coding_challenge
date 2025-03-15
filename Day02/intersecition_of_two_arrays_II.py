#leetcode: 350. Intersection of Two Arrays II
#https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution(object):
    def intersect(self, nums1, nums2):
        count = {}
        
        # Count occurrences of elements in nums1
        for num in nums1:
            count[num] = count.get(num, 0) + 1#count the frequency of each element in the first list
        
        result = []
        
        # Check elements of nums2 against the count dictionary
        for num in nums2:
            if count.get(num, 0) > 0:#if the element is present in the count dictionary
                result.append(num)#append the element to the result list
                count[num] -= 1  # Decrement count to maintain frequency
        
        return result

# Taking input from the user
nums1 = list(map(int, input("Enter numbers for the first list separated by space: ").split()))
nums2 = list(map(int, input("Enter numbers for the second list separated by space: ").split()))

# Creating an instance of Solution class
solution = Solution()

# Calling intersect function
result = solution.intersect(nums1, nums2)

# Printing the intersection of both lists considering frequency
print("Intersection of both lists:", result)
