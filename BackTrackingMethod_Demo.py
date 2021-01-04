class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if (len(matrix) <= 0 or rows < 1 or cols < 1 or len(path) <= 0):
            return False
        visted = [[0 for j in range(cols)] for i in range(rows)]
        pathLength = 0
        for i in range(rows):
            for j in range(cols):
                if (self.hasPathCore(matrix, rows, cols, i, j, path, pathLength, visted)):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visted):
        if (pathLength >= len(path)):
            return True

        hasPath = False
        if (row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] == path[pathLength] and
                visted[row][col] == 0):
            pathLength += 1
            visted[row][col] = 1
            hasPath = (self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathLength, visted) or
                       self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathLength, visted) or
                       self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathLength, visted) or
                       self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathLength, visted))
            if (hasPath == False):
                pathLength -= 1
                visted[row][col] = 0
        return hasPath

if __name__ == '__main__':
    s = Solution()
    matrix,path = "aa","aa"
    print(s.hasPath(matrix,1,2,path))