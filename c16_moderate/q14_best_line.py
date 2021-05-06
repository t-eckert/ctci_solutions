"""
16.14 Best Line: Given a two-dimensional graph with points on it, find a line
  which passes through the most number of points.
"""

"""
  Assuming that the points are integer tuples.
"""
import random as rd
import matplotlib.pyplot as plt
import operator
import numpy as np


def generate_random_points(n_points):
    points = []
    for point in range(n_points):
        x = rd.randint(-100000, 100000)
        y = rd.randint(-100000, 100000)
        points.append((x, y))
    return points


def calculate_mb(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    # handle the infinite slope
    if x2 != x1:
        m = (y2 - y1) / (x2 - x1)
        b = y2 - m * x2
        return m, b
    else:
        return "inf", "dne"


def find_best_line(points):
    lines = {}

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            m, b = calculate_mb(points[i], points[j])
            if (m, b) in lines.keys():
                lines[(m, b)] += 1
            else:
                lines[(m, b)] = 1

    return max(lines.items(), key=operator.itemgetter(1))[0]


def abline(m, b):
    x_vals = np.array([i for i in range(-100000, 100000)])
    y_vals = b + m * x_vals
    return x_vals, y_vals


def main():
    points = generate_random_points(100)
    m, b = find_best_line(points)
    x, y = zip(*points)
    if type(m) is float and type(b) is float:
        x_line, y_line = abline(m, b)
        plt.plot(x_line, y_line)
    else:
        print("The line has an infinite slope.")
    plt.scatter(x, y)
    plt.show()


main()
