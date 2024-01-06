class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if r in rows or c in cols:
                    matrix[r][c] = 0