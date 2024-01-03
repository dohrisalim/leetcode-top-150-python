class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        s = s.split(" ")

        for word in s[::-1]:
            if word:
                result += word + " "
        return result[:-1]