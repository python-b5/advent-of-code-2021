###################
# Day 15 - Chiton #
# Part 2          #
###################


# Imports
import heapq
from itertools import chain


class Node:
    """Single A* node."""
    def __init__(self, parent, position, g, h, f):
        self.parent = parent
        self.position = position

        self.g = g
        self.h = h
        self.f = f

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.g < other.g


# Overflow number based on limit
def overflow(n, limit):
    remainder = n % limit
    return [remainder, limit][not remainder]


# Find adjacent locations
def adjacent(data, x, y):
    output = []

    if x > 0: output.append((x - 1, y))
    if x < len(data[y]) - 1: output.append((x + 1, y))
    if y > 0: output.append((x, y - 1))
    if y < len(data) - 1: output.append((x, y + 1))

    return output


# Pathfind with A*
def pathfind(data, start, end):
    start_node = Node(None, start, 0, 0, 0)
    end_node = Node(None, end, 0, 0, 0)

    open_ = [start_node]
    closed = set()
    traveled = set()

    heapq.heapify(open_)

    while True:
        current_node = heapq.heappop(open_)

        if current_node == end_node:
            return current_node.g
        else:
            closed.add(current_node)

        adj = adjacent(
            data,
            current_node.position[0],
            current_node.position[1]
        )

        for pos in adj:
            child = Node(
                current_node,
                pos,
                g := current_node.g + data[pos[1]][pos[0]],
                h := (
                    abs(end_node.position[0] - pos[0])
                    + abs(end_node.position[1] - pos[1])
                ),
                g + h
            )

            if child not in traveled and child not in closed:
                heapq.heappush(open_, child)
                traveled.add(child)


def main():
    # Load input
    with open("inputs/day_15.txt") as file:
        data = [[int(n) for n in line] for line in file.read().split("\n")]

    # Find path
    total_risk = pathfind(data, (0, 0), (len(data[0]) - 1, len(data) - 1))

    # Output results
    print(f"Total risk: {total_risk}")


# Run script
if __name__ == "__main__":
    main()
