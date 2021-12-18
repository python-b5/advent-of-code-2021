#######################
# Day 17 - Trick Shot #
# Part 1              #
#######################


# Simulate a trajectory and calculate whether it falls within a target position
def simulate(x, y, xvel, yvel, x_range, y_range):
    max_y = min(0, min(y_range))

    while x <= x_range[-1] and y >= y_range[0]:
        if x in x_range and y in y_range:
            return {
                "in_range": True,
                "max_y": max_y
            }

        x += xvel
        y += yvel

        if y > max_y:
            max_y = y

        if xvel > 0:
            xvel -= 1
        elif xvel < 0:
            xvel += 1

        yvel -= 1

    return {
        "in_range": False,
        "max_y": max_y
    }


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

    max_yvel = min(0, min(y_range))
    highest_point = None

    for xvel in range(0, max(x_range) * 2):
        for yvel in range(min(0, min(y_range)), max(y_range) * -2):
            simulation_results = simulate(0, 0, xvel, yvel, x_range, y_range)

            if simulation_results["in_range"] and yvel > max_yvel:
                max_yvel = yvel
                highest_point = simulation_results["max_y"]


    # Output results
    print(f"Highest point: {highest_point}")


# Run script
if __name__ == "__main__":
    main()
