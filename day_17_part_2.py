#######################
# Day 17 - Trick Shot #
# Part 2              #
#######################


# Simulate a trajectory and calculate whether it falls within a target position
def simulate(x, y, xvel, yvel, x_range, y_range):
    while x <= x_range[-1] and y >= y_range[0]:
        if x in x_range and y in y_range:
            return True

        x += xvel
        y += yvel

        if xvel > 0:
            xvel -= 1
        elif xvel < 0:
            xvel += 1

        yvel -= 1

    return False


def main():
    # Load input
    with open("inputs/day_17.txt") as file:
        data = [
            [int(coord) for coord in coords] for coords in [
                coords[2:].split("..")
                for coords in file.read()[13:].split(", ")
            ]
        ]

    # Find trajectories
    x_range = range(data[0][0], data[0][1] + 1)
    y_range = range(data[1][0], data[1][1] + 1)

    valid_velocities = []

    for xvel in range(0, max(x_range) * 2):
        for yvel in range(min(0, min(y_range)), max(y_range) * -2):
            if simulate(0, 0, xvel, yvel, x_range, y_range):
                valid_velocities.append((xvel, yvel))

    # Output results
    print(f"Valid velocities: {len(valid_velocities)}")


# Run script
if __name__ == "__main__":
    main()
