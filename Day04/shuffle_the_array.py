# LeetCode Problem Number: 384
# Problem Link: https://leetcode.com/problems/shuffle-an-array/

import random

class Solution(object):

    def __init__(self, nums):
        """
        Initializes the Solution object with the given array.
        
        :param nums: List[int] - The input array of numbers.
        """
        self.original = nums[:]  # Store a copy of the original array

    def reset(self):
        """
        Resets the array to its original configuration and returns it.
        
        :return: List[int] - The original array.
        """
        return self.original  # Return the original array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        
        :return: List[int] - A shuffled version of the array.
        """
        shuffled = self.original[:]
        for i in range(len(shuffled)):
            swap_index = random.randrange(i, len(shuffled))  # Pick a random index from i to end
            shuffled[i], shuffled[swap_index] = shuffled[swap_index], shuffled[i]  # Swap elements
        return shuffled

# Taking user input
input_list = list(map(int, input("Enter numbers (space-separated): ").split()))
solution = Solution(input_list)

# Printing shuffled array
print("\nShuffled Array:", solution.shuffle())

# Resetting and printing the original array
print("Reset Array:", solution.reset())

# Time Complexity: O(n) - Fisher-Yates Algorithm
# Space Complexity: O(n) - Stores original array

