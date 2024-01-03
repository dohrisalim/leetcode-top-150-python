class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        p = 0
        strs = sorted(strs)
        while (p < len(strs[0])):
            temp = strs[0][p]
            for i in range(len(strs)):
                if strs[i][p] != temp:
                    return result

            result += temp
            p+=1 

        return result