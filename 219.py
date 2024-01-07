class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            
            if num in seen:
                temp = abs(i - seen[num])
                if temp <= k:
                    return True
                

            seen[num] = i
        return False