class Solution:
    def canJump(self, nums):
        furthest_reach = 0
        for i, num in enumerate(nums):
            if i > furthest_reach:
                return False
            furthest_reach = max(furthest_reach, i + num)
            if furthest_reach >= len(nums) - 1:
                return True
        return False