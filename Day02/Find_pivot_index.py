#leetcode: 724. Find Pivot Index
#https://leetcode.com/problems/find-pivot-index/
class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)#calculate the total sum of the list
        left_sum = 0

        for i, num in enumerate(nums):#enumerate the list
            if left_sum == (total_sum - left_sum - num):#if the left sum is equal to the right sum then return the index
                return i
            left_sum += num#increment the left sum
        
        return -1

# Taking input from the user
nums = list(map(int, input("Enter the numbers separated by space: ").split()))

# Creating an instance of Solution class
solution = Solution()

# Calling pivotIndex function
result = solution.pivotIndex(nums)

# Printing the result
print("Pivot Index:", result)
