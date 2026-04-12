from typing import List
from collections import Counter

class CountSquares:

    def __init__(self):
        self.points = []
        self.point_counts = Counter()

    def add(self, point: List[int]) -> None:
        self.points.append(tuple(point))
        self.point_counts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0

        for px, py in self.points:
            # check for same y but different x (horizontal side of a square)
            if py == y and px != x:
                side = abs(px - x)

                # Check the two corresponding vertical points
                p1 = (x, y + side)
                p2 = (px, y + side)
                p3 = (x, y - side)
                p4 = (px, y - side)

                # Square above
                result += self.point_counts[p1] * self.point_counts[p2]
                # Square below
                result += self.point_counts[p3] * self.point_counts[p4]

        return result
