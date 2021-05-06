import math
import random
from operator import itemgetter


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathFinder:
    def __init__(self, terrain, initial_point, final_point):
        self.terrain_latitude = len(terrain[0])
        self.terrain_longitude = len(terrain)
        self.visited_points = [
            [False for i in range(self.terrain_latitude)]
            for j in range(self.terrain_longitude)
        ]
        self.current_location = initial_point
        self.final_location = final_point

    def update_current_location(self, location):
        self.current_location = location

    def mark_as_visited(self, point):
        self.visited_points[point.x][point.y] = True

    def is_point_in_terrain(self, point):
        if (
            point.x > self.terrain_latitude
            or point.x < 0
            or point.y > self.terrain_longitude
            or point.y < 0
        ):
            return False
        return True

    def is_on_west_edge(self, point):
        return point.x == 0

    def is_on_east_edge(self, point):
        return point.x == self.terrain_latitude - 1

    def is_on_north_edge(self, point):
        return point.y == 0

    def is_on_south_edge(self, point):
        return point.y == self.terrain_longitude - 1

    def is_on_northwest_corner(self, point):
        return self.is_on_north_edge(point) and self.is_on_west_edge(point)

    def is_on_northeast_corner(self, point):
        return self.is_on_north_edge(point) and self.is_on_east_edge(point)

    def is_on_southwest_corner(self, point):
        return self.is_on_south_edge(point) and self.is_on_west_edge(point)

    def is_on_southeast_corner(self, point):
        return self.is_on_south_edge(point) and self.is_on_east_edge(point)

    def get_adjacent_points(self):
        point = self.current_location
        X = self.current_location.x
        Y = self.current_location.y

        north = Point(X, Y - 1)
        south = Point(X, Y + 1)
        west = Point(X - 1, Y)
        east = Point(X + 1, Y)
        northwest = Point(X - 1, Y - 1)
        northeast = Point(X + 1, Y - 1)
        southwest = Point(X - 1, Y + 1)
        southeast = Point(X + 1, Y + 1)

        if self.is_on_northwest_corner(point):
            return [east, southeast, south]
        elif self.is_on_northeast_corner(point):
            return [west, southwest, south]
        elif self.is_on_southwest_corner(point):
            return [east, northeast, north]
        elif self.is_on_southeast_corner(point):
            return [west, northwest, north]
        elif self.is_on_north_edge(point):
            return [west, southwest, south, southeast, east]
        elif self.is_on_south_edge(point):
            return [west, northwest, north, northeast, east]
        elif self.is_on_west_edge(point):
            return [north, northeast, east, southeast, south]
        elif self.is_on_east_edge(point):
            return [north, northwest, west, southwest, south]
        else:
            return [
                north,
                northeast,
                east,
                southeast,
                south,
                southwest,
                west,
                northwest,
            ]


def calculate_distance(point_a, point_b):
    delta_x = abs(point_a.x - point_b.x)
    delta_y = abs(point_a.y - point_b.y)
    return math.sqrt(delta_x ** 2 + delta_y ** 2)


def create_terrain(latitude, longitude):
    return [[random.randint(0, 10) for i in range(latitude)] for j in range(longitude)]


def rank_point(point, final_point, mire):
    distance_to_final = calculate_distance(point, final_point)
    rank = distance_to_final + mire
    return [rank, point]


def rank_points(points, final_point, terrain):
    ranked_points: list = []
    for point in points:
        mire = terrain[point.x][point.y]
        ranked_points.append(rank_point(point, final_point, mire))
    return ranked_points


def sort_ranked_points(ranked_points):
    return sorted(ranked_points, key=itemgetter(0))
