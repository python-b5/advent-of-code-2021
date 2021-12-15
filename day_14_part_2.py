####################################
# Day 14 - Extended Polymerization #
# Part 2                           #
####################################


class Simulation:
    """Simulates polymerization."""
    def __init__(self, polymer, insertions):
        polymer_pairs = [
            "".join(pair) for pair in zip(polymer, polymer[1:])
        ]

        self.polymer = {}

        for pair in set(polymer_pairs):
            self.polymer[pair] = polymer_pairs.count(pair)

        self.elements = {
            element:polymer.count(element) for element in set(polymer)
        }

        self.insertions = insertions

    def step(self):
        """Runs a step of the simulation."""
        new_polymer = dict(self.polymer)

        for insertion in self.insertions:
            if insertion in self.polymer and self.polymer[insertion]:
                self.add(
                    new_polymer,
                    insertion[0] + self.insertions[insertion],
                    self.polymer[insertion]
                )

                self.add(
                    new_polymer,
                    self.insertions[insertion] + insertion[1],
                    self.polymer[insertion]
                )

                self.add(
                    self.elements,
                    self.insertions[insertion],
                    self.polymer[insertion]
                )

                new_polymer[insertion] -= self.polymer[insertion]

        self.polymer = new_polymer

    def add(self, l, i, n):
        """
        Adds a number to a dictionary index.
        Creates the index if it doesn't exist.
        """
        if i in l:
            l[i] += n
        else:
            l[i] = n


def main():
    # Load input
    with open("inputs/day_14.txt") as file:
        data = file.read().split("\n")

    # Parse input
    polymer_start = data[0]
    insertions = dict(insertion.split(" -> ") for insertion in data[2:])

    # Initialize simulation
    polymer = Simulation(polymer_start, insertions)

    # Run steps
    for step in range(40):
        polymer.step()

    # Output results
    elements = polymer.elements.values()
    print(f"Difference of quantities: {max(elements) - min(elements)}")


# Run script
if __name__ == "__main__":
    main()
