# leetcode : 1
#enumerate(): The enumerate() function in Python is used to iterate over an iterable while keeping track of the index of each element.
#  It returns an index-element pair for each iteration.

class Solution:
    def twosum(self,nums,target):
        previmap={}#dictionary to store thr index and the differeence number 
        for i,n in enumerate(nums):
            diff=target-n#calculated the difference btween the  target the iterating number
            if diff in previmap:#if the target is already existing in the previous map return it
                return [previmap[diff],i]
            previmap[n]=i#else store the number and the index in the dictionary
        return None
    
nums=list(map(int,input("enter the number seperated by the:").split()))
target=int(input("enter the target"))

solution=Solution()

result=solution.twosum(nums,target)
print(result)
    
