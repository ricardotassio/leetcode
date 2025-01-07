class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for idx, item in enumerate(nums):
            comp = target - item
            if comp in seen:
                return [seen[comp],idx]
            seen[item] = idx