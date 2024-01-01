class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize the second pointer
        k = 0
        # Iterate over the array
        for i in range(len(nums)):
            # If the current element is not equal to val
            if nums[i] != val:
                # Place it at the position indicated by the second pointer
                nums[k] = nums[i]
                # Increment the second pointer
                k += 1
        # Return the number of elements not equal to val
        return k