class Solution(object):
    def validmountainarra(self,arr):
        left,right=0,len(arr)-1
        while left<right:
            if arr[left]<arr[left+1]:
                left+=1
            elif arr[right]<arr[right-1]:
                right-=1
            else:
                break
        return left==right and (left>0 and right<len(arr)-1)