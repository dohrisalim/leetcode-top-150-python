class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        temp = {}
        for char in magazine:
            if char in temp:
                temp[char] += 1
            else:
                temp[char] = 1
        
        for char in ransomNote:
            if char in temp:
                if temp[char] > 0:
                    temp[char] -= 1
                else:
                    return False
            else:
                return False

        return True