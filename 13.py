class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        p = 0
        length = len(s)
        while p < length:
            if p+1 < length and roman_to_int[s[p]] < roman_to_int[s[p+1]]:
                result += roman_to_int[s[p+1]] - roman_to_int[s[p]]
                p += 2
            else:
                result += roman_to_int[s[p]]
                p += 1
        return result