'''
16.19 Pond Sizes: You have an integer matrix representing a plot of land where 
    the value at that location represents the height above sea level. A value
    of zero indicates water. A pond is a region of water connected vertically,
    horizontally, or diagonally. The size of the pond is the total number of 
    connected water cells. Write a method to compute the sizes of all ponds in
    the matrix.
'''
import random as r

def create_land():
    n = r.randint(1,25)
    m = r.randint(1,25)
    return [[r.randint(0,2) for i in range(n)] for j in range(m)]

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
    n = len(land) -1
    m = len(land[0]) -1
    if i == 0 or i == n or j == 0 or j == m:
        search_area = edge_helper(i, j, land)
    else:
        search_area = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    around = 8 -len(search_area)
    for k,l in search_area:
        if land[i+k][j+l] == 0 and checked_matrix[i+k][j+l] == 0:
            # print("Looking around")
            lake_size, checked_matrix = find_water(i+k, j+l, land, checked_matrix, lake_size+1)
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
            return [(0,1),(1,0),(1,1)]
        elif j == len(land[0])-1:
            # top right corner
            return [(0,-1),(1,-1),(1,0)]
        else:
            # top row
            return [(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    elif i == len(land)-1:
        if j == 0:
            # bottom left corner
            return [(-1,0),(-1,1),(0,1)]
        elif j == len(land[0])-1:
            # bottom right corner
            return [(-1,-1),(-1,0),(0,-1)]
        else: 
            # bottom row
            return [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1)]
    elif j == 0:
        # left column
        return [(-1,0),(-1,1),(0,1),(1,0),(1,1)]
    else:
        # right column
        return [(-1,-1),(-1,0),(0,-1),(1,-1),(1,0)]

def print_land(land):
    n = len(land)
    m = len(land[0])
    for i in range(n):
        for j in range(m):
            print("[%s][%s] %s" % (i, j, land[i][j]))

def main():
    # land = create_land()
    land = [[1,1,2,2,1,0,0,1,2,3,2,2,2,1,2,1,1,1,1,0,0,0]
,[1,1,1,2,1,0,0,1,2,3,3,2,1,2,2,1,1,0,0,0,1,1]
,[2,1,0,0,1,1,0,1,1,2,0,2,1,1,2,1,2,1,1,1,1,0]
,[1,0,0,1,1,1,1,2,2,1,0,0,1,2,2,1,2,2,1,1,1,1]
,[0,0,1,1,2,1,2,2,1,1,0,0,1,2,1,1,2,2,1,1,1,2]
,[0,1,1,2,1,2,2,2,1,1,1,1,2,1,1,2,2,1,1,1,2,1]
,[1,1,0,1,1,2,2,1,1,1,2,2,2,2,1,2,1,1,1,2,2,1]
,[2,1,1,1,1,1,2,1,1,0,1,1,0,1,0,1,2,1,1,1,2,2]
,[1,1,0,1,0,0,1,1,0,0,1,1,1,0,1,1,1,1,2,1,2,1]
,[0,0,1,1,1,0,1,1,0,1,1,1,0,1,1,2,1,1,1,1,1,1]
,[0,0,1,2,1,1,1,1,1,1,0,1,1,2,1,0,0,1,1,0,1,1]
,[0,1,1,2,1,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,1,2]
,[1,1,2,1,1,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,1,1]
,[2,1,1,1,1,1,1,2,1,1,1,0,0,0,1,0,0,1,1,0,1,1]
,[1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,2,1,0,0,1]
,[1,1,1,1,2,2,1,2,1,1,1,0,0,0,0,0,1,2,1,1,0,1]]
    for row in land:
        print(row)
    print("\n"+str(lakes_in(land)))

main()