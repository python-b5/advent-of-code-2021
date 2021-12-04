#######################
# Day 4 - Giant Squid #
# Part 1              #
#######################


class Board:
    """Stores a board of Numbers."""
    def __init__(self, lines):
        self.board = []

        for line in lines:
            self.board.append([Number(n) for n in line.split()])

    def check(self, number):
        """Checks the board for a number, and marks it if found."""
        for line in self.board:
            for n in line:
                if n.number == number:
                    n.marked = True

    @property
    def won(self):
        """Checks the board to see if it has been won."""
        return any(
            any(all(n.marked for n in line) for line in board) for board in [
                self.board,
                [*zip(*self.board)]
            ]
        )

    def score(self, last_called):
        """Calculates the board's score based on the last called number."""
        return sum(
            sum(n.number for n in line if not n.marked) for line in self.board
        ) * last_called


class Number:
    """Stores a number that can be marked."""
    def __init__(self, number):
        self.number = int(number)
        self.marked = False


def main():
    # Load input
    with open("inputs/day_4.txt") as file:
        data = file.read().split("\n")

    # Parse input
    data = list(filter(lambda line: line, data))
    queue = [int(n) for n in data[0].split(",")]

    boards = []
    for i in range(1, len(data), 5):
        boards.append(Board(data[i:i + 5]))

    # Simulate game
    for n in queue:
        for i, board in enumerate(boards):
            board.check(n)

            if board.won:
                # Output results
                print(f"Board {i + 1} won!")
                print(f"Final score: {board.score(n)}")

                return


# Run script
if __name__ == "__main__":
    main()
