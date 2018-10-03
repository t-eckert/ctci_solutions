import math


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
        X = self.current_location.x
        Y = self.current_location.y

        north = [X, Y - 1]
        south = [X, Y + 1]
        west = [X - 1, Y]
        east = [X + 1, Y]
        northwest = [X - 1, Y - 1]
        northeast = [X + 1, Y - 1]
        southwest = [X - 1, Y + 1]
        southeast = [X + 1, Y + 1]

        if self.is_on_northwest_corner(point):
            return [east, southeast, south]
        elif self.is_on_northeast_corner(point):
            return [west, southwest, south]

    def calculate_distance(self, point_a, point_b):
        delta_x = abs(point_a.x - point_b.x)
        delta_y = abs(point_a.y - point_b.y)
        return math.sqrt(delta_x ** 2 + delta_y ** 2)
