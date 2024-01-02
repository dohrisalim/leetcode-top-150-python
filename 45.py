class Solution:
    def jump(self, nums):
        jumps = 0
        end = 0
        furthest_jump = 0
        for i in range(len(nums) - 1):
            furthest_jump = max(furthest_jump, i + nums[i])
            if i == end:
                jumps += 1
                end = furthest_jump
        return jumps