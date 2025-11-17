# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Using the binary search finding the minimum number. In the first case checked the mid is minimum than previous and next element if this condition satisfies then return it. Else check the array is left or righ sorted and move the pointer accordingly. Time Complexity O(log n)

class Solution:
    def findMin(self, nums : list[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            # very first check if the left is smaller than the right. it means array is sorted and we got the minimum number
            if nums[low] <= nums[high]:
                return nums[low]
            mid = (low + high) // 2 
            # this  "or" condition is the edge case along with that check the mid is smaller than the previous and smaller than the nex
            if (mid == 0 or nums[mid] < nums[mid - 1]) and (mid == high - 1 or nums[mid]< nums[mid+1]):
                return nums[mid]
            # this condition means left half is sorted
            elif nums[low] <= nums[mid]:
                # so as the element is not in the left side move the pointer to right. why element is not in the left side because we already check the low in very first condition after while
                low = mid + 1
            # when the left is not sorted means right is sorted so move the pointer to the left part
            else:
                high = mid - 1
        return nums[low]
    
sh = Solution()
print(sh.findMin([3,4,5,1,2]))    
print(sh.findMin([4,5,6,7,0,1,2]))    
print(sh.findMin([11,13,15,17]))    
                


        