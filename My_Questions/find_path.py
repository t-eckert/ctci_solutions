import PathFinding

"""
    Goal: Find the path through the terrain that minimizes cost to mire.
    Algorithm:
        0. begin at any point in the terrain
        1. assess which points surround current point
        2. rank those points according to mire cost and closeness to goal
        3. travel to point with lowest rank
"""

terrain = [
    [2, 6, 0, 1, 2],
    [1, 5, 4, 10, 8],
    [4, 4, 6, 3, 9],
    [8, 0, 1, 6, 1],
    [6, 3, 3, 3, 6],
    [0, 8, 10, 5, 1],
    [1, 5, 2, 8, 5],
    [3, 7, 3, 6, 1],
]

starting_point = PathFinding.Point(0, 0)
final_point = PathFinding.Point(5, 8)

path_finder = PathFinding.PathFinder(terrain, starting_point, final_point)



def search():
    path_finder.mark_as_visited(path_finder.current_location)
    for row in path_finder.visited_points:
        print(row)

    adjacent_points = path_finder.get_adjacent_points()
    ranked_adj_pts = PathFinding.rank_points(adjacent_points, final_point, terrain)
    ordered_adj_pts = PathFinding.sort_ranked_points(ranked_adj_pts)

    print("Ordered adjacent points:")
    for point in ordered_adj_pts:
        print(f"{point[0]}: {point[1].x}, {point[1].y}")

    path_finder.update_current_location(ordered_adj_pts[0][1])
    print(f"Moving to {ordered_adj_pts[0][1].x}, {ordered_adj_pts[0][1].x}")


search()
search()
search()
search()