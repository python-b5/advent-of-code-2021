#######################
# Day 6 - Lanternfish #
# Part 1              #
#######################


class Simulation:
    """Simulates lanternfish reproduction."""
    def __init__(self, fish):
        self.fish = [fish.count(n) for n in range(9)]
    
    def step(self):
        """Runs a step of the simulation."""
        new_fish = [*self.fish]
        
        for i in range(len(self.fish) - 1, -1, -1):
            if i < len(self.fish) - 1:
                if i == 0 and self.fish[i] > 0:
                    new_fish[6] += self.fish[i]
                    new_fish[8] += self.fish[i]
                
                new_fish[i] = self.fish[i + 1]
            else:
                new_fish[i] = 0

        self.fish = new_fish


def main():
    # Load input
    with open("inputs/day_6.txt") as file:
        data = [int(n) for n in file.read().split(",")]
    
    # Initialize simulation
    simulation = Simulation(data)
    
    # Simulate lanternfish for 80 days
    for _ in range(80):
        simulation.step()
    
    # Output results
    print(f"Lanternfish count: {sum(simulation.fish)}")


# Run script
if __name__ == "__main__":
    main()