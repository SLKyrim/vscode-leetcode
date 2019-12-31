# -*- coding: utf-8 -*-
"""
Created on 2019/12/27 17:07



Author: Long
"""


class UnionFind:
    def __init__(self, index):
        self.roots = []
        for i in range(index):
            self.roots.append(i)

    def findRoot(self, index):
        # There must be a root in self.roots equals its own index
        while self.roots[index] != index:
            self.roots[index] = self.roots[self.roots[index]]
            index = self.roots[index]
        return index

    def union(self, index1, index2):
        root1 = self.findRoot(index1)
        root2 = self.findRoot(index2)
        if root1 != root2:
            self.roots[root1] = root2

    def isConnected(self, index1, index2):
        return self.findRoot(index1) == self.findRoot(index2)


class Solution:

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def xyTo1D(row, col):
            return row * cols + col

        uf = UnionFind(rows * cols + 1)
        # make the last position as a dummyNode connects the O on edge
        dummyNode = rows * cols

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1):
                        uf.union(xyTo1D(i, j), dummyNode)
                    elif i - 1 >= 0 and board[i - 1][j] == 'O':
                        uf.union(xyTo1D(i, j), xyTo1D(i - 1, j))
                    elif i + 1 < rows and board[i + 1][j] == 'O':
                        uf.union(xyTo1D(i, j), xyTo1D(i + 1, j))
                    elif j - 1 >= 0 and board[i][j - 1] == 'O':
                        uf.union(xyTo1D(i, j), xyTo1D(i, j - 1))
                    elif j + 1 < cols and board[i][j + 1] == 'O':
                        uf.union(xyTo1D(i, j), xyTo1D(i, j + 1))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and not uf.isConnected(xyTo1D(i, j), dummyNode):
                    board[i][j] = 'X'


if __name__ == '__main__':
    s = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    s.solve(board)