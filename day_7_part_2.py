###################################
# Day 7 - The Treachery of Whales #
# Part 2                          #
###################################


def main():
    # Load input
    with open("inputs/day_7.txt") as file:
        data = [int(n) for n in file.read().split(",")]

    # Find cheapest alignment position
    scores = []

    for alignment in range(max(data)):
        score = 0

        for n in data:
            raw_score = abs(n - alignment)
            score += (raw_score ** 2 + raw_score) / 2

        scores.append(score)

    # Output results
    print(f"Fuel cost: {int(min(scores))}")


# Run script
if __name__ == "__main__":
    main()