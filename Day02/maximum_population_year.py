#leetcode: 1854. Maximum Population Year
#https://leetcode.com/problems/maximum-population-year/
class Solution(object):
    def maximumPopulation(self, logs):
        year_counts = {}#dictionary to store the population per year

        # Count population per year
        for birth, death in logs:
            for year in range(birth, death):#iterate over the years between birth and death
                year_counts[year] = year_counts.get(year, 0) + 1#increment the population count for each year
        
        # Return the earliest year with the maximum population
        return min(year_counts, key=lambda y: (-year_counts[y], y))#return the year with the maximum population

# Taking input from the user
n = int(input("Enter the number of logs: "))
logs = []

for _ in range(n):
    birth, death = map(int, input("Enter birth and death year separated by space: ").split())
    logs.append((birth, death))

# Creating an instance of Solution class
solution = Solution()

# Calling maximumPopulation function
result = solution.maximumPopulation(logs)

# Printing the year with the maximum population
print("Year with maximum population:", result)
# Time complexity: O(n)
# Space complexity: O(n)
