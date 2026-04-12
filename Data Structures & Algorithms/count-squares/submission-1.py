class CountSquares:

    def __init__(self):
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points.append(tuple(point))

    def count(self, point: List[int]) -> int:
        if not self.points:
            return 0

        freq_points = Counter(self.points)
        count = 0

        x, y = point
        for px, py in self.points:
            if (abs(px - x) != abs(py-y)) or x == px or y == py:
                continue
            print(px, py)
            count += freq_points[(px, y)] * freq_points[(x, py)]
            
            

        return count
