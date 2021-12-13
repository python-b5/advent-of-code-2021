############################
# Day 12 - Passage Pathing #
# Part 1                   #
############################


def main():
    # Load input
    with open("inputs/day_12.txt") as file:
        data = [
            connection.split("-") for connection in file.read().split("\n")
        ]

    # Find connections
    connections = {"end": []}

    for connection in data:
        for i, cave in enumerate(connection):
            if cave != "end":
                if cave not in connections:
                    connections[cave] = []

                connections[cave].append(connection[not i])

    # Find paths
    paths = [["start"]]
    completed_paths = []

    while True:
        new_paths = []

        for path in paths:
            valid_connections = [
                connection for connection in connections[path[-1]]
                if connection.isupper() or connection not in path
            ]

            if valid_connections:
                for connection in valid_connections:
                    if connection == "end":
                        completed_paths.append(path + [connection])
                    else:
                        new_paths.append(path + [connection])
            else:
                new_paths.append(path)

        if new_paths == paths:
            break
        else:
            paths = new_paths

    # Output results
    print(f"Paths: {len(completed_paths)}")


# Run script
if __name__ == "__main__":
    main()
