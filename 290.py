class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words, temp = s.split(' '), dict()

        if len(pattern) != len(words): return False
        if len(set(pattern)) != len(set(words)): return False 

        for i in range(len(words)):
            if words[i] not in temp: 
                temp[words[i]] = pattern[i]
            elif temp[words[i]] != pattern[i]: 
                return False

        return True