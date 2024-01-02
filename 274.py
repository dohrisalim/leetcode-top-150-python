class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        h_index = 0
        citationLength = len(citations)
        for i in range(citationLength):
            if i + 1  <= citations[i]:
                h_index = i +1
            else:
                break

        return h_index