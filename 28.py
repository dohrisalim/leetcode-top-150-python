class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            result = haystack.find(needle)
            return result
        else:
            return -1