#######################
# Day 1 - Sonar Sweep #
# Part 1              #
#######################


def main():
    # Load input
    with open("inputs/day_1.txt") as file:
        data = [int(n) for n in file.read().split("\n")]

    # Counter for increases
    increases = 0

    # Loop through data to check for increases
    last = None
    for i in data:
        if last != None:
            if i > last:
                increases += 1

        last = i

    # Output results
    print(f"Increases: {increases}")


# Run script
if __name__ == "__main__":
    main()
