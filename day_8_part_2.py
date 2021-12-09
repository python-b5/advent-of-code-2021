################################
# Day 8 - Seven Segment Search #
# Part 2                       #
################################


# Imports
from itertools import product


# Translate
def translate(segment, alphabet, choices):
    return set(
        sorted(list(alphabet[letter]))[
            choices[list(alphabet).index(letter)]
            if len(alphabet[letter]) > choices[list(alphabet).index(letter)]
            else -1
        ] for letter in segment
    )


def main():
    # Load input
    with open("inputs/day_8.txt") as file:
        data = [entry.split(" | ") for entry in file.read().split("\n")]

        for entry in data:
            for i, values in enumerate(entry):
                entry[i] = values.split(" ")

    # Numbers
    numbers = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9"
    }

    # Valid 6 length segments
    length_6 = [
        set(list(numbers.keys())[0]),
        set(list(numbers.keys())[6]),
        set(list(numbers.keys())[9])
    ]

    # Translate output values
    output_values = []

    for entry in data:
        possible_matches = {letter: set() for letter in "abcdefg"}

        segments = {}

        for n in (2, 3, 4):
            segments[n] = next(
                segment for segment in entry[0] if len(segment) == n
            )

        segments[6] = [segment for segment in entry[0] if len(segment) == 6]

        for letter in segments[2]:
            possible_matches[letter].update(set("cf"))

        possible_matches[
            list(set(segments[3]) - set(segments[2]))[0]
        ].update(set("a"))

        for letter in set(segments[4]) - set(segments[2]):
            possible_matches[letter].update(set("bd"))

        unused_letters = [
            letter for letter in "abcdefg" if not possible_matches[letter]
        ]

        for letter in unused_letters:
            possible_matches[letter].update(set("eg"))

        for choices in product((0, 1), repeat=7):
            if all(
                    translate(segment, possible_matches, choices) in length_6
                    for segment in segments[6]
            ):
                break

        output_values.append(
            int("".join(
                numbers[
                    "".join(sorted(list(
                        translate(segment, possible_matches, choices)
                    )))
                ] for segment in entry[1]
            ))
        )

    # Output results
    print(f"Sum of output values: {sum(output_values)}")


# Run script
if __name__ == "__main__":
    main()
