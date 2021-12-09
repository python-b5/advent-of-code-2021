################################
# Day 8 - Seven Segment Search #
# Part 1                       #
################################


def main():
    # Load input
    with open("inputs/day_8.txt") as file:
        data = [entry.split(" | ") for entry in file.read().split("\n")]

        for entry in data:
            for i, values in enumerate(entry):
                entry[i] = values.split(" ")

    # Find unique segment numbers
    unique_segments = 0

    for entry in data:
        for segment in entry[1]:
            if len(segment) in (2, 4, 3, 7):
                unique_segments += 1

    # Output results
    print(f"Unique segments: {unique_segments}")


# Run script
if __name__ == "__main__":
    main()
