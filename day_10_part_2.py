###########################
# Day 10 - Syntax Scoring #
# Part 2                  #
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

    # Find scores
    scores = []

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
                    break
    
        if expected and not corrupted:
            score = 0
            
            for char in reversed(expected):
                score *= 5
                score += ")]}>".index(char) + 1
            
            scores.append(score)
    
    # Output results
    print(f"Middle score: {median(scores)}")


# Run script
if __name__ == "__main__":
    main()
