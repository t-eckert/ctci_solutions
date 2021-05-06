"""
16.19 Pond Sizes: You have an integer matrix representing a plot of land where 
    the value at that location represents the height above sea level. A value
    of zero indicates water. A pond is a region of water connected vertically,
    horizontally, or diagonally. The size of the pond is the total number of 
    connected water cells. Write a method to compute the sizes of all ponds in
    the matrix.
"""
import random as r

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class LakeFinder:

    def __init__(self, terrain):
        self.terrain = terrain
        self.terrain_latitude = len(terrain[0])
        self.terrain_longitude = len(terrain)
        self.visited_points = [
            [False for i in range(self.terrain_latitude)]
            for j in range(self.terrain_longitude)
        ]
        self.lake_sizes = []
        self.current_point = None

    def in_terrain(self, point: Point):
        X = point.x
        Y = point.y

        return (
            X >= 0 and
            Y >= 0 and
            X < self.terrain_latitude and
            Y < self.terrain_longitude
        )

    def set_visited(self, point):
        self.visited_points[point.x][point.y] = True

    def is_point_visited(self, point):
        return self.visited_points[point.x][point.y]

    def set_current_point(self, point):
        if self.in_terrain(point):
            self.current_point = point

    def on_west_edge(self):
        return self.current_point.x == 0

    def on_east_edge(self):
        return self.current_point.x == self.terrain_latitude - 1

    def on_north_edge(self):
        return self.current_point.y == 0

    def on_south_edge(self):
        return self.current_point.y == self.terrain_longitude - 1

    def on_northwest_corner(self):
        return self.on_north_edge() and self.on_west_edge()

    def on_northeast_corner(self):
        return self.on_north_edge() and self.on_east_edge()

    def on_southwest_corner(self):
        return self.on_south_edge() and self.on_west_edge()

    def on_southeast_corner(self):
        return self.on_south_edge() and self.on_east_edge()

    def get_adjacent_points(self):
        X = self.current_point.x
        Y = self.current_point.y

        north = Point(X, Y - 1)
        south = Point(X, Y + 1)
        west = Point(X - 1, Y)
        east = Point(X + 1, Y)
        northwest = Point(X - 1, Y - 1)
        northeast = Point(X + 1, Y - 1)
        southwest = Point(X - 1, Y + 1)
        southeast = Point(X + 1, Y + 1)

        if self.on_northwest_corner():
            return [east, southeast, south]
        elif self.on_northeast_corner():
            return [west, southwest, south]
        elif self.on_southwest_corner():
            return [east, northeast, north]
        elif self.on_southeast_corner():
            return [west, northwest, north]
        elif self.on_north_edge():
            return [west, southwest, south, southeast, east]
        elif self.on_south_edge():
            return [west, northwest, north, northeast, east]
        elif self.on_west_edge():
            return [north, northeast, east, southeast, south]
        elif self.on_east_edge():
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

    def print_terrain(self):
        for row in self.terrain:
            print(row)

    def unvisited_points(self, points):
        unvisited_points = []
        for point in points:
            if not self.is_point_visited(point):
                unvisited_points.append(point)
        return unvisited_points

    def is_water(self, point):
        return self.terrain[point.x][point.y] == 0

    def wet_points(self, points):
        wet_points = []
        for point in points:
            if self.is_water(point):
                wet_points.append(point)
        return wet_points

    def search_completed(self):
        for row in self.terrain:
            if False in row:
                return False
        else: 
            return True

    def search(self):
        # breakpoint()
        while not self.search_completed():
            self.search_for_water()

    def search_for_water(self):
        # breakpoint()
        if self.current_point is None:
            origin_point = Point(0,0)
            self.set_current_point(origin_point)
        self.set_visited(self.current_point)
        if self.is_water(self.current_point):
            self.lake_sizes.append(1)
            self.explore_lake()
        adjacent_points = self.get_adjacent_points()
        possible_points = self.unvisited_points(adjacent_points)
        if len(possible_points) == 0:
            print("Done searching for water")
            return None
        next_point = possible_points[0]
        self.set_current_point(next_point)

    def explore_lake(self):
        adjacent_points = self.get_adjacent_points()
        surrounding_water = self.unvisited_points(self.wet_points(adjacent_points))
        if len(surrounding_water) == 0:
            return None
        self.lake_sizes[-1] += len(surrounding_water)
        for water_point in surrounding_water:
            self.set_current_point(water_point)


def lakes_in(land):
    lake_sizes = []
    n = len(land)
    m = len(land[0])
    checked_matrix = [[0 for i in range(m)] for j in range(n)]
    # for row in checked_matrix:
    #     print(row)
    for i in range(n):
        for j in range(m):
            if land[i][j] == 0 and checked_matrix[i][j] == 0:
                # print("Checking %s %s" % (i,j))
                lake_size, checked_matrix = find_water(i, j, land, checked_matrix, 1)
                lake_sizes.append(lake_size)
            else:
                checked_matrix[i][j] = 1
    return lake_sizes


def find_water(i, j, land, checked_matrix, lake_size):
    # print("In find_water with %s %s" % (i, j))
    checked_matrix[i][j] = 1
    n = len(land) - 1
    m = len(land[0]) - 1
    if i == 0 or i == n or j == 0 or j == m:
        search_area = edge_helper(i, j, land)
    else:
        search_area = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
    around = 8 - len(search_area)
    for k, l in search_area:
        if land[i + k][j + l] == 0 and checked_matrix[i + k][j + l] == 0:
            # print("Looking around")
            lake_size, checked_matrix = find_water(
                i + k, j + l, land, checked_matrix, lake_size + 1
            )
            around += 1
        else:
            around += 1
    if around == 8:
        return lake_size, checked_matrix


def edge_helper(i, j, land):
    if len(land) == 1:
        return []
    if i == 0:
        if j == 0:
            # top left corner
            return [(0, 1), (1, 0), (1, 1)]
        elif j == len(land[0]) - 1:
            # top right corner
            return [(0, -1), (1, -1), (1, 0)]
        else:
            # top row
            return [(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    elif i == len(land) - 1:
        if j == 0:
            # bottom left corner
            return [(-1, 0), (-1, 1), (0, 1)]
        elif j == len(land[0]) - 1:
            # bottom right corner
            return [(-1, -1), (-1, 0), (0, -1)]
        else:
            # bottom row
            return [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1)]
    elif j == 0:
        # left column
        return [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, 1)]
    else:
        # right column
        return [(-1, -1), (-1, 0), (0, -1), (1, -1), (1, 0)]


def print_land(land):
    n = len(land)
    m = len(land[0])
    for i in range(n):
        for j in range(m):
            print("[%s][%s] %s" % (i, j, land[i][j]))


def create_land():
    n = r.randint(1, 25)
    m = r.randint(1, 25)
    return [[r.randint(0, 2) for i in range(n)] for j in range(m)]


def main():
    # land = create_land()
    land = [
        [1, 1, 2, 2, 1, 0, 0, 1, 2, 3, 2, 2, 2, 1, 2, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 2, 1, 0, 0, 1, 2, 3, 3, 2, 1, 2, 2, 1, 1, 0, 0, 0, 1, 1],
        [2, 1, 0, 0, 1, 1, 0, 1, 1, 2, 0, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 0],
        [1, 0, 0, 1, 1, 1, 1, 2, 2, 1, 0, 0, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1],
        [0, 0, 1, 1, 2, 1, 2, 2, 1, 1, 0, 0, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2],
        [0, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1],
        [1, 1, 0, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1],
        [2, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 0, 1, 2, 1, 1, 1, 2, 2],
        [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 2, 1, 2, 1],
        [0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 2, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 1, 1, 0, 1, 1],
        [0, 1, 1, 2, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 2],
        [1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
        [2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 2, 1, 0, 0, 1],
        [1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1],
    ]
    for row in land:
        print(row)
    print("\n" + str(lakes_in(land)))


main()
