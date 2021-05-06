import unittest
from q19_Pond_Sizes import LakeFinder, Point

test_terrain = [
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

class TestLakeFinder(unittest.TestCase):
    def test_in_terrain(self):
        # arrange
        test_point = Point(1,1)
        test_lake_finder = LakeFinder(test_terrain)

        # act
        point_in_terrain = test_lake_finder.in_terrain(test_point)

        # assert
        self.assertTrue(point_in_terrain)

    def test_lake_sizes(self):
        # arrange
        test_lake_finder = LakeFinder(test_terrain)

        expected_lake_sizes = [5, 6, 7, 5, 1, 1, 4, 4, 6, 3, 35, 4, 2]

        # act
        test_lake_finder.search()
        lake_sizes = test_lake_finder.lake_sizes

        # assert
        self.assertEqual(expected_lake_sizes, lake_sizes)

TestLakeFinder().test_lake_sizes()