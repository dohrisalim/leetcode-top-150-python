class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            s = str(n)
            temp = 0
            for char in s:
                temp += int(char) * int(char)
            if temp in seen:
                return False

            seen.add(n)
            n = temp
            if n == 1:
                return True

        return False