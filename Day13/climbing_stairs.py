#leetcode: 70. Climbing Stairs
#https://leetcode.com/problems/climbing-stairs/
class Solution(object):
    def climbStairs(self, n):
        prev=1
        prev2=0
        for i in range(1,n+1):
            curi=prev + prev2
            prev2 = prev
            prev = curi
        return prev
# Taking input from user
n = int(input("Enter number of stairs: "))