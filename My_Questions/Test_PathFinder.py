import unittest
from PathFinding import PathFinder, Point

test_terrain = [
    [2, 1, 3, 0, 0, 2, 9, 1, 2, 0],
    [2, 1, 4, 6, 6, 3, 2, 4, 2, 1],
    [2, 1, 3, 0, 0, 2, 9, 1, 2, 0],
    [9, 2, 1, 5, 5, 2, 3, 1, 1, 1],
    [2, 1, 3, 0, 0, 2, 9, 1, 2, 0],
    [2, 1, 4, 6, 6, 3, 2, 4, 2, 1],
    [2, 1, 3, 0, 0, 2, 9, 1, 2, 0],
    [9, 2, 1, 5, 5, 2, 3, 1, 1, 1],
    [2, 1, 3, 0, 0, 2, 9, 1, 2, 0],
    [2, 1, 4, 6, 6, 3, 2, 4, 2, 1],
    [2, 1, 3, 0, 0, 2, 9, 1, 2, 0],
    [9, 2, 1, 5, 5, 2, 3, 1, 1, 1],
    [2, 1, 3, 0, 0, 2, 9, 1, 2, 0],
    [2, 1, 4, 6, 6, 3, 2, 4, 2, 1],
    [2, 1, 3, 0, 0, 2, 9, 1, 2, 0],
    [9, 2, 1, 5, 5, 2, 3, 1, 1, 1],
]
test_initial_point = Point(0, 0)
test_final_point = Point(10, 10)


class Test_PathFinder(unittest.TestCase):
    def test_update_current_location(self):
        # arrange
        expected_location = Point(5, 5)

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )

        test_path_finder.update_current_location(expected_location)

        # assert
        self.assertEqual(expected_location, test_path_finder.current_location)

    def test_visited_points_init(self):
        # arrange
        expected_latitude = len(test_terrain)
        expected_longitude = len(test_terrain[0])

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )
        actual_latitude = len(test_path_finder.visited_points)
        actual_longitude = len(test_path_finder.visited_points[0])

        # assert
        self.assertEqual(expected_latitude, actual_latitude)
        self.assertEqual(expected_longitude, actual_longitude)

    def test_no_points_visited(self):
        # arrange
        expected_visited_points = [
            [False for i in range(len(test_terrain[0]))]
            for j in range(len(test_terrain))
        ]

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )

        # assert
        self.assertEqual(expected_visited_points, test_path_finder.visited_points)

    def test_mark_as_visited(self):
        # arrange
        test_x = 2
        test_y = 3
        test_visted_point = Point(test_x, test_y)

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )
        test_path_finder.mark_as_visited(test_visted_point)

        # assert
        self.assertTrue(test_path_finder.visited_points[test_x][test_y])

    def test_is_point_in_terrain_out_west(self):
        # arrange
        test_x = -1
        test_y = 3
        test_point = Point(test_x, test_y)

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )

        # assert
        self.assertFalse(test_path_finder.is_point_in_terrain(test_point))

    def test_is_point_in_terrain_out_east(self):
        # arrange
        test_x = len(test_terrain[0]) + 20
        test_y = 3
        test_point = Point(test_x, test_y)

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )

        # assert
        self.assertFalse(test_path_finder.is_point_in_terrain(test_point))

    def test_is_on_west_edge(self):
        # arrange
        test_x = 0
        test_y = 3
        test_point = Point(test_x, test_y)

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )

        # assert
        self.assertTrue(test_path_finder.is_on_west_edge(test_point))

    def test_is_on_east_edge(self):
        # arrange
        test_x = 9
        test_y = 3
        test_point = Point(test_x, test_y)

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )

        # assert
        self.assertTrue(test_path_finder.is_on_east_edge(test_point))

    def test_is_on_north_edge(self):
        # arrange
        test_x = 3
        test_y = 0
        test_point = Point(test_x, test_y)

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )

        # assert
        self.assertTrue(test_path_finder.is_on_north_edge(test_point))

    def test_is_on_south_edge(self):
        # arrange
        test_x = 3
        test_y = 15
        test_point = Point(test_x, test_y)

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )

        # assert
        self.assertTrue(test_path_finder.is_on_south_edge(test_point))

    def test_is_on_northwest_corner(self):
        # arrange
        test_x = 0
        test_y = 0
        test_point = Point(test_x, test_y)

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )

        # assert
        self.assertTrue(test_path_finder.is_on_northwest_corner(test_point))

    def test_is_on_northeast_corner(self):
        # arrange
        test_x = 9
        test_y = 0
        test_point = Point(test_x, test_y)

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )

        # assert
        self.assertTrue(test_path_finder.is_on_northeast_corner(test_point))

    def test_is_on_southwest_corner(self):
        # arrange
        test_x = 0
        test_y = 15
        test_point = Point(test_x, test_y)

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )

        # assert
        self.assertTrue(test_path_finder.is_on_southwest_corner(test_point))

    def test_is_on_southeast_corner(self):
        # arrange
        test_x = 9
        test_y = 15
        test_point = Point(test_x, test_y)

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )

        # assert
        self.assertTrue(test_path_finder.is_on_southeast_corner(test_point))

    def test_calculate_distance(self):
        # arrange
        test_point_a = Point(2, 4)
        test_point_b = Point(8, 9)
        expected_distance = 7.810249675906654

        # act
        test_path_finder = PathFinder(
            test_terrain, test_initial_point, test_final_point
        )
        actual_distance = test_path_finder.calculate_distance(
            test_point_a, test_point_b
        )

        # assert
        self.assertEqual(expected_distance, actual_distance)
