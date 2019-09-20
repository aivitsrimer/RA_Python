from math import *

from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


def to_vector(a: Point) -> tuple:
    return a.x, a.y


def to_json(a: Point) -> str:
    import json
    return json.dumps({
        'x': a.x,
        'y': a.y,
    })


def distance(a: Point, b: Point) -> float:
    return sqrt((b.x - a.x) ** 2 + ((b.y - a.y) ** 2))


p = Point(3, 4)
print(distance(p, Point(-98.8, 7)))
print(to_vector(p))
print(to_json(p))
