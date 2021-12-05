################################
# Day 5 - Hydrothermal Venture #
# Part 2                       #
################################


# Imports
from collections import Counter


# Get sign of number, returning 1 if sign is 0
def sign(n):
    if n < 0:
        return -1
    else:
        return 1


def main():
    # Load input
    with open("inputs/day_5.txt") as file:
        data = file.read().split("\n")

    # Parse input
    data = [
        [tuple(int(n) for n in pair.split(",")) for pair in segment]
        for segment in [line.split(" -> ") for line in data]
    ]

    # Find all coordinates in segments
    points = []
    for i, segment in enumerate(data):
        x_positions = (segment[0][0], segment[1][0])
        y_positions = (segment[0][1], segment[1][1])

        x_sign = sign(x_positions[1] - x_positions[0])
        y_sign = sign(y_positions[1] - y_positions[0])

        x_range = range(x_positions[0], x_positions[1] + x_sign, x_sign)
        y_range = range(y_positions[0], y_positions[1] + y_sign, y_sign)

        if x_positions[0] == x_positions[1]:
            points += [(x_positions[0], y) for y in y_range]
        elif y_positions[0] == y_positions[1]:
            points += [(x, y_positions[0]) for x in x_range]
        else:
            points += list(zip(x_range, y_range))

    # Find intersections
    counts = Counter(points)
    intersections = [point for point in counts if counts[point] > 1]

    # Output results
    print(f"Number of intersections: {len(intersections)}")


# Run script
if __name__ == "__main__":
    main()
