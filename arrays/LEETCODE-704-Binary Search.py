### 704. Binary Research
# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.
# Initialize the left and right pointers
# While left is less than or equal to right
# Find the middle element
# If the middle element is the target, return the index
# If the middle element is less than the target, move the left pointer to mid + 1
# If the middle element is greater than the target, move the right pointer to mid - 1
# Return -1 if the target is not found

class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums)-1

        while l<= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        return -1