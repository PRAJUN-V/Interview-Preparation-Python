from dataclasses import dataclass

@dataclass
class Coordinate:
    x: int
    y: int

point1 = Coordinate(1, 2)
point2 = Coordinate(3, 4)
print(point1)
