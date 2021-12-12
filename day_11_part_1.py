##########################
# Day 11 - Dumbo Octopus #
# Part 1                 #
##########################


# Find adjacent octopuses
def adjacent(data, x, y):
    output = []

    if x > 0: output.append((x - 1, y))
    if x < len(data[y]) - 1: output.append((x + 1, y))
    if y > 0: output.append((x, y - 1))
    if y < len(data) - 1: output.append((x, y + 1))

    if (x + 1, y) in output and (x, y + 1) in output:
        output.append((x + 1, y + 1))

    if (x + 1, y) in output and (x, y - 1) in output:
        output.append((x + 1, y - 1))

    if (x - 1, y) in output and (x, y - 1) in output:
        output.append((x - 1, y - 1))

    if (x - 1, y) in output and (x, y + 1) in output:
        output.append((x - 1, y + 1))

    return output


# Flash octopuses
def flash(flashes, data, x, y):
    flashes.append((x, y))

    for pos in adjacent(data, x, y):
        if (pos[0], pos[1]) not in flashes:
            data[pos[1]][pos[0]] += 1

            if data[pos[1]][pos[0]] > 9:
                flash(flashes, data, pos[0], pos[1])


def main():
    # Load input
    with open("inputs/day_11.txt") as file:
        data = [[int(n) for n in line] for line in file.read().split("\n")]

    # Simulate octopus flashes
    flashes_count = 0

    for step in range(100):
        flashes = []

        data = [[n + 1 for n in line] for line in data]

        for y, line in enumerate(data):
            for x, n in enumerate(line):
                if n > 9 and (x, y) not in flashes:
                    flash(flashes, data, x, y)

        for pos in flashes:
            data[pos[1]][pos[0]] = 0

        flashes_count += len(flashes)

    # Output results
    print(f"Total flashes: {flashes_count}")


# Run script
if __name__ == "__main__":
    main()
