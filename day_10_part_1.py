###########################
# Day 10 - Syntax Scoring #
# Part 1                  #
###########################


# Imports
from statistics import median


def main():
    # Load input
    with open("inputs/day_10.txt") as file:
        data = file.read().split("\n")
    
    # Bracket matches
    matches = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }

    # Error scores
    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    # Find errors
    error_score = 0

    for line in data:
        expected = []
        corrupted = False
        
        for char in line:
            if char in "([{<":
                expected.append(matches[char])
            elif char in ")]}>":
                if expected[-1] == char:
                    expected = expected[:-1]
                else:
                    corrupted = True
                    error_score += scores[char]
                    break
    
    # Output results
    print(f"Syntax error score: {error_score}")


# Run script
if __name__ == "__main__":
    main()
