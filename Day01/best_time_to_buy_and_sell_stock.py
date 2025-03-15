#leetcode: 121. Best Time to Buy and Sell Stock
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution(object):
    def maxProfit(self, prices):
        min_val = float('inf')#initialize the minimum value to infinity
        maxprof = 0
        for price in prices:
            min_val = min(min_val, price)#find the minimum value
            maxprof = max(maxprof, price - min_val)#find the maximum profit
        return maxprof

prices = list(map(int, input("Enter stock prices separated by space: ").split()))

# Creating an instance of Solution class
solution = Solution()

# Calling maxProfit function and printing result
print("Maximum Profit:", solution.maxProfit(prices))
# Time complexity: O(n)
# Space complexity: O(1)

