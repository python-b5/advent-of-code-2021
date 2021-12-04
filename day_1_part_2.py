#######################
# Day 1 - Sonar Sweep #
# Part 2              #
#######################


def main():
    # Load input
    with open("inputs/day_1.txt") as file:
        data = [int(n) for n in file.read().split("\n")]

    # Counter for increases
    increases = 0

    # Loop through data to check for increases
    last = None
    for i in range(len(data) - 2):
        current = data[i] + data[i + 1] + data[i + 2]

        if last != None:
            if current > last:
                increases += 1

        last = current

    # Output results
    print(f"Increases: {increases}")


# Run script
if __name__ == "__main__":
    main()
