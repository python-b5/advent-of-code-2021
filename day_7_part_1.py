###################################
# Day 7 - The Treachery of Whales #
# Part 1                          #
###################################


def main():
    # Load input
    with open("inputs/day_7.txt") as file:
        data = [int(n) for n in file.read().split(",")]

    # Find cheapest alignment position
    scores = []

    for alignment in range(max(data)):
        score = sum(abs(n - alignment) for n in data)
        scores.append(score)

    # Output results
    print(f"Fuel cost: {int(min(scores))}")


# Run script
if __name__ == "__main__":
    main()