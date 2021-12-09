#######################
# Day 9 - Smoke Basin #
# Part 1              #
#######################


# Find adjacent locations on heightmap
def adjacent(data, x, y):
    output = []

    if x > 0: output.append((x - 1, y))
    if x < len(data[y]) - 1: output.append((x + 1, y))
    if y > 0: output.append((x, y - 1))
    if y < len(data) - 1: output.append((x, y + 1))

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

    # Output results
    print(f"Sum of risk levels: "
        f"{sum(data[coords[1]][coords[0]] + 1 for coords in low_points)}"
    )


# Run script
if __name__ == "__main__":
    main()
