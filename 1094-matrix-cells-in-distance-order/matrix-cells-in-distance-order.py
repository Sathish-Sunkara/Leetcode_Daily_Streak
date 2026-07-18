class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cords = ([[x,y] for x in range(rows) for y in range(cols)])
        cords = sorted(cords , key = lambda cell : abs(rCenter-cell[0]) + abs(cCenter-cell[1]))

        return (cords)
        