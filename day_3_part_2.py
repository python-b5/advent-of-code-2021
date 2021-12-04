#############################
# Day 3 - Binary Diagnostic #
# Part 2                    #
#############################


# Get most common item in list of 1s and 0s (prefer 1)
def max_binary(l):
    if l.count("0") > l.count("1"):
        return "0"
    else:
        return "1"


# Get least common item in list of 1s and 0s (prefer 0)
def min_binary(l):
    if l.count("1") < l.count("0"):
        return "1"
    else:
        return "0"


def main():
    # Load input
    with open("inputs/day_3.txt") as file:
        data = file.read().split("\n")

    # Clone data into rating lists
    generator_rating = data
    scrubber_rating = data

    # Calculate ratings
    for i in range(len(max(data, key=len))):
        most_common = max_binary([n[i] for n in generator_rating])
        least_common = min_binary([n[i] for n in scrubber_rating])

        if len(generator_rating) > 1:
            generator_rating = list(filter(lambda n: n[i] == most_common, generator_rating))

        if len(scrubber_rating) > 1:
            scrubber_rating = list(filter(lambda n: n[i] == least_common, scrubber_rating))

    # Convert rates to decimal
    generator_rating = int(generator_rating[0], base=2)
    scrubber_rating = int(scrubber_rating[0], base=2)

    # Output results
    print(f"Oxygen generator rating: {generator_rating}")
    print(f"CO2 scrubber rating: {scrubber_rating}")
    print(f"Final result (multiplied): {generator_rating * scrubber_rating}")


# Run script
if __name__ == "__main__":
    main()
