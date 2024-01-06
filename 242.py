class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stemp, ttemp = dict(), dict()
        for char in s:
            if char in stemp:
                stemp[char] += 1
            else:
                stemp[char] = 1

        for char in t:
            if char in ttemp:
                ttemp[char] += 1
            else:
                ttemp[char] = 1

        if len(stemp) != len(ttemp): return False

        for char in stemp:
            if char in ttemp:
                if stemp[char] != ttemp[char]: return False
            else:
                return False

        return True