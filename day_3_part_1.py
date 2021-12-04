#############################
# Day 3 - Binary Diagnostic #
# Part 1                    #
#############################


def main():
    # Load input
    with open("inputs/day_3.txt") as file:
        data = file.read().split("\n")

    # Organize into columns
    columns = []
    for column in range(len(max(data, key=len))):
        columns.append([n[column] for n in data])

    # Calculate rates
    gamma_rate = ""
    epsilon_rate = ""

    for column in columns:
        gamma_rate += max(set(column), key=column.count)
        epsilon_rate += min(set(column), key=column.count)

    # Convert rates to decimal
    gamma_rate = int(gamma_rate, base=2)
    epsilon_rate = int(epsilon_rate, base=2)

    # Output results
    print(f"Gamma rate: {gamma_rate}")
    print(f"Epsilon rate: {epsilon_rate}")
    print(f"Final result (multiplied): {gamma_rate * epsilon_rate}")


# Run script
if __name__ == "__main__":
    main()
