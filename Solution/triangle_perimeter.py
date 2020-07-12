from math import sqrt


def cut_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def triangle_perimetr(AB, AC, BC):
    return AB + AC + BC

x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x3, y3 = int(input()), int(input())

AB = cut_distance(x1, y1, x2, y2)
AC = cut_distance(x3, y3, x1, y1)
BC = cut_distance(x3, y3, x2, y2)

print(triangle_perimetr(AB, AC, BC))
