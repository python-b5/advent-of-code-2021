#######################
# Day 9 - Smoke Basin #
# Part 2              #
#######################


# Imports
from math import prod


# Flatten list
def flatten(l):
    return [item for sublist in l for item in sublist]


# Find adjacent locations on heightmap
def adjacent(data, x, y, higher=False):
    output = []

    if x > 0: output.append((x - 1, y))
    if x < len(data[y]) - 1: output.append((x + 1, y))
    if y > 0: output.append((x, y - 1))
    if y < len(data) - 1: output.append((x, y + 1))

    if higher:
        return [
            location for location in output
            if data[location[1]][location[0]] - data[y][x] >= 1
        ]
    else:
        return output


def main():
    # Load input
    with open("inputs/day_9.txt") as file:
        data = [
            [int(location) for location in list(row)]
            for row in file.read().split("\n")
        ]
    
    # Find low points
    low_points = []

    for y, row in enumerate(data):
        for x, location in enumerate(row):
            if all(
                data[other[1]][other[0]] > location
                for other in adjacent(data, x, y)
            ):
                low_points.append((x, y))

    # Find basins
    basins = []

    for x, y in low_points:
        basin_locations = [(x, y)]
        new_locations = [(x, y)]

        while new_locations:
            new_locations = list(set([
                coords for coords in flatten(
                    adjacent(data, coords[0], coords[1], higher=True)
                    for coords in new_locations
                ) if coords not in basin_locations
                and data[coords[1]][coords[0]] < 9
            ]))

            basin_locations += new_locations
        
        basins.append(basin_locations)

    # Output results
    basin_sizes = [len(basin) for basin in basins]
    
    print(f"Largest basins (multiplied): {prod(sorted(basin_sizes)[-3:])}")


# Run script
if __name__ == "__main__":
    main()
