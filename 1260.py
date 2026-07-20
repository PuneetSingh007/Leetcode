#shift-2d-grid
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        nums = m * n
        p = k % nums

        list1 = []
        for i in grid:
            for j in i:
                list1.append(j)

        newlist = list1[nums-p:] + list1[:nums-p]

        Grid = [[0] * n for _ in range(m)]

        l = 0
        start = 0
        end = n

        for i in range(m):
            Grid[l] = newlist[start:end]
            l += 1
            start = end
            end += n

        return Grid