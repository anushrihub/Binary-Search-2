# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# this first and last is not the first half and last half but its the first and last number of the consecutive intergers 
# we are providing the (high = mid - 1) condition twice in row no. 18 and 21 because 18 number is for the consecutive numbers first part and second is for the normal binary search on entire list

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binarySearchFirst(nums, target, low, high):
            while low <= high:
                mid = (low + high) // 2
                # when the mid is target element
                if nums[mid] == target:
                # this condition gives us the first position
                # once we get the mid as a target check the previous is not a target or target is at zero position means there is no previous
                    if nums[mid-1] != target or mid == 0:
                        return mid
                # but if the mid - 1 is also target element then change the high pointer and calculate the first from the previous
                    else:
                        high = mid -1
                # search the target in the left half
                elif nums[mid] > target:
                    high = mid - 1
                # search the target in the right half
                else:
                    low = mid + 1
            return -1
    
        def binarySearchLast(nums, target, low, high):
            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    # this condition gives us the last position
                    # once we get the mid as a target check the next is not a target or target is at the last position means there is next
                    if nums[mid + 1] != target or mid == len(nums)-1:
                        return mid
                    else:
                        low = mid + 1
                elif nums[mid] > target:
                    high = mid -1
                else:
                    low = mid + 1
            return -1

        first = binarySearchFirst(nums, target, 0 , len(nums)-1 )
        if first == -1:
            return [-1, -1]
        else:
            # first occurance of this function must be the last occurance of target so here we are provided the first as a low
            last = binarySearchLast(nums, target, first, len(nums)-1)
        return [first, last] 




sh = Solution()
print(sh.searchRange([5,7,7,8,8,10],8))
print(sh.searchRange([5,7,7,8,8,10],7))
print(sh.searchRange([],0))
