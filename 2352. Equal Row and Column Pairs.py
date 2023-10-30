class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowdict = {}
        coldict = {}
        n = len(grid)
        for i in range(n):
            row = ""
            col = ""
            for j in range(n):
                row += "," + str(grid[i][j])
                col += "," + str(grid[j][i])
            if row in rowdict:
                rowdict[row] += 1
            else:
                rowdict[row] = 1
            if col in coldict:
                coldict[col] += 1
            else:
                coldict[col] = 1
        count = 0
        for i in rowdict:
            if i in coldict:
                count += rowdict[i] * coldict[i]
        return count
