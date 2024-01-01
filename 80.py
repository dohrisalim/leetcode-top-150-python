class Solution:
    def removeDuplicates(self, nums):
        # If the array has less than or equal to two elements, return its length
        if len(nums) <= 2:
            return len(nums)

        # Initialize the second pointer
        k = 2
        # Iterate over the array, starting from the third element
        for i in range(2, len(nums)):
            # If the current element is different from the one before the previous one
            if nums[i] != nums[k - 2]:
                # Place it at the position indicated by the second pointer
                nums[k] = nums[i]
                # Increment the second pointer
                k += 1
        # Return the number of elements after removing duplicates
        return k