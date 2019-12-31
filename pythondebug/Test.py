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

    def getRoots(self):
        for i in range(len(self.roots)):
            self.roots[i] = self.findRoot(i)
        return self.roots


class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        def xyTo1D(row, col):
            return row * cols + col

        uf = UnionFind(rows * cols + 1)
        # make the last position as a dummyNode presents 0 (water)
        dummyNode = rows * cols

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0":
                    uf.union(xyTo1D(i, j), dummyNode)
                else:
                    if i - 1 >= 0 and grid[i - 1][j] == "1":
                        uf.union(xyTo1D(i, j), xyTo1D(i - 1, j))
                    if i + 1 < rows and grid[i + 1][j] == "1":
                        uf.union(xyTo1D(i, j), xyTo1D(i + 1, j))
                    if j - 1 >= 0 and grid[i][j - 1] == "1":
                        uf.union(xyTo1D(i, j), xyTo1D(i, j - 1))
                    if j + 1 < cols and grid[i][j + 1] == "1":
                        uf.union(xyTo1D(i, j), xyTo1D(i, j + 1))

        roots = uf.getRoots()
        return len(set(roots)) - 1


if __name__ == '__main__':
    s = Solution()
    board = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(s.numIslands(board) - 1)