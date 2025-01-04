class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = set()

        for i,val in enumerate(nums):
            if i > k:
                seen.remove(nums[i-k-1])
            if val in seen:
                return True
        
            seen.add(val)
        return False