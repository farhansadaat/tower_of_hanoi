"""Interactive Tower of Hanoi game."""

NUM_DISKS = 3
COLUMN_NAMES = ("A", "B", "C")


def new_game(num_disks):
    return {
        "A": list(range(num_disks, 0, -1)),
        "B": [],
        "C": [],
    }


def print_board(columns, num_disks):
    print()
    for row in range(num_disks - 1, -1, -1):
        cells = []
        for name in COLUMN_NAMES:
            column = columns[name]
            cells.append(str(column[row]) if row < len(column) else " ")
        print(" | ".join(cells))
    print()


def read_column(prompt):
    choice = input(prompt).strip().upper()
    if choice not in COLUMN_NAMES:
        print(f"Please enter one of {', '.join(COLUMN_NAMES)}.")
        return None
    return choice


def move_disk(columns, source, destination):
    if not columns[source]:
        print(f"Column {source} is empty.")
        return False

    disk = columns[source][-1]
    if columns[destination] and columns[destination][-1] < disk:
        print("You can't place a larger disk on a smaller one.")
        return False

    columns[destination].append(columns[source].pop())
    return True


def is_solved(columns, num_disks):
    return len(columns["B"]) == num_disks or len(columns["C"]) == num_disks


def main():
    print("Tower of Hanoi")
    print("Enter a column (A, B, or C) to move the top disk from, then a column to move it to.")
    print("A larger disk can never be placed on a smaller one.")
    print(f"Goal: move the entire stack of {NUM_DISKS} disks off column A.")

    columns = new_game(NUM_DISKS)
    moves = 0

    while not is_solved(columns, NUM_DISKS):
        print_board(columns, NUM_DISKS)

        source = read_column("Move from column? ")
        if source is None:
            continue

        destination = read_column("Move to column? ")
        if destination is None:
            continue

        if source == destination:
            print("Source and destination must be different.")
            continue

        if move_disk(columns, source, destination):
            moves += 1

    print_board(columns, NUM_DISKS)
    print(f"Congratulations! You solved it in {moves} moves.")


if __name__ == "__main__":
    main()
