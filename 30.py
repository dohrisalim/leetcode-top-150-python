from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        
        word_len = len(words[0])
        words_len = len(words) * word_len
        words_counter = Counter(words)
        res = []
        
        for i in range(len(s) - words_len + 1):
            seen = Counter()
            for j in range(i, i + words_len, word_len):
                curr_word = s[j:j + word_len]
                if curr_word in words_counter:
                    seen[curr_word] += 1
                    if seen[curr_word] > words_counter[curr_word]:
                        break
                else:
                    break
            else:
                res.append(i)
                
        return res