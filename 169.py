class Solution:
    def majorityElement(self, nums):
        candidate = nums[0]
        count = 0

        for num in nums:
            if num == candidate:
                count += 1
            else:
                count -= 1

            if count == 0:
                candidate = num
                count = 1

            if count >= len(nums)/2:
                return candidate

        return candidate
