class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        for char in s:
            if char.isalnum():
                temp += char

        for i in range(len(temp)):
            if temp[i].lower() != temp[len(temp) - (i + 1)].lower():
                return False

        return True