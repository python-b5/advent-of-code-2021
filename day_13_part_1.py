################################
# Day 13 - Transparent Origami #
# Part 1                       #
################################


def main():
    # Load input
    with open("inputs/day_13.txt") as file:
        data = file.read().split("\n\n")
    
    # Parse input
    points = [
        [int(coord) for coord in point.split(",")]
        for point in data[0].split("\n")
    ]

    folds = [
        [int(char) if char.isdigit() else char for char in fold[11:].split("=")]
        for fold in data[1].split("\n")
    ]

    # Complete first fold
    fold = folds[0]
    
    if fold[0] == "x": fold_axis = 0
    else: fold_axis = 1

    affected_points = [point for point in points if point[fold_axis] > fold[1]]

    for point in affected_points:
        points.remove(point)
        
        mirror_length = point[fold_axis] - fold[1]
        point[fold_axis] = fold[1] - mirror_length

        if point not in points:
            points.append(point)
    
    # Output results
    print(f"Visible points: {len(points)}")


# Run script
if __name__ == "__main__":
    main()
