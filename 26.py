class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 0
        for i, num in enumerate(nums[1:], start=1):
            if num != nums[k]:
                k += 1
                nums[k] = num
        return k + 1