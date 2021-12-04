#################
# Day 2 - Dive! #
# Part 2        #
#################


def main():
    # Load input
    with open("inputs/day_2.txt") as file:
        data = file.read().split("\n")

    # Parse input
    instructions = []

    for line in data:
        line_split = line.split(" ")
        instructions.append({
            "type": line_split[0],
            "value": int(line_split[1])
        })

    # Initialize variables
    pos = 0
    depth = 0
    aim = 0

    # Loop through instructions
    for instruction in instructions:
        if instruction["type"] == "forward":
            pos += instruction["value"]
            depth += aim * instruction["value"]
        elif instruction["type"] == "down":
            aim += instruction["value"]
        elif instruction["type"] == "up":
            aim -= instruction["value"]

    # Output results
    print(f"Final position: {pos}")
    print(f"Final depth: {depth}")
    print(f"Final result (multiplied): {pos * depth}")


# Run script
if __name__ == "__main__":
    main()
