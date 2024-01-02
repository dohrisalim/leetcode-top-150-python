class Solution:
    def candy(self, ratings):
        n = len(ratings)
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        return sum(max(l, r) for l, r in zip(left, right))