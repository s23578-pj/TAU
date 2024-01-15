"""Terminal game for testing edge cases and checking GitHub Actions"""
import random

"""Game presents 5x5 grid where the player move using W, A, S or D keys. Game ends when player finds a treasure."""
rows = 5
cols = 5

number_of_obstacles = random.randint(5, rows * cols // 4)


def generate_board(rows, cols):
    board = [['-' for _ in range(cols)] for _ in range(rows)]

    start_row = random.choice([0, rows - 1])
    start_col = random.randint(0, cols - 1)
    start = (start_row, start_col)

    stop_row = random.choice([row for row in [0, rows - 1] if row != start_row])
    stop_col = random.randint(0, cols - 1)
    stop = (stop_row, stop_col)

    board[start[0]][start[1]] = 'A'
    board[stop[0]][stop[1]] = 'B'

    for _ in range(number_of_obstacles):
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        while board[row][col] in ['A', 'B', 'X']:
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)

        board[row][col] = 'X'

    return board, start, stop


def display_board(board, current_position):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if (i, j) == current_position:
                print('@', end=' ')
            else:
                print(cell, end=' ')
        print()


def make_move(board, current_position, move):
    new_position = current_position

    if move == 'W' and current_position[0] > 0:
        if board[current_position[0] - 1][current_position[1]] != 'X':
            new_position = (current_position[0] - 1, current_position[1])
    elif move == 'S' and current_position[0] < len(board) - 1:
        if board[current_position[0] + 1][current_position[1]] != 'X':
            new_position = (current_position[0] + 1, current_position[1])
    elif move == 'A' and current_position[1] > 0:
        if board[current_position[0]][current_position[1] - 1] != 'X':
            new_position = (current_position[0], current_position[1] - 1)
    elif move == 'D' and current_position[1] < len(board[0]) - 1:
        if board[current_position[0]][current_position[1] + 1] != 'X':
            new_position = (current_position[0], current_position[1] + 1)
    elif move == 'Q':
        print("Exiting the game. See you later!")
        exit()

    if new_position == current_position:
        print("Invalid move! Try again.")

    return new_position


def move(board, start, stop):
    current_position = start

    while True:
        display_board(board, current_position)
        move = input("Where to move? (W A S D): ").upper()
        new_position = make_move(board, current_position, move)

        if new_position == current_position:
            print("Invalid move! Try again. Hint: W -> Up, A -> Left, S -> Down, D -> Right. "
                  "Warning: make sure you are using uppercase")
        elif new_position == stop:
            print("Congratulations! You reached the destination!")
            break
        else:
            current_position = new_position


def start_game(rows, cols):
    board, start, stop = generate_board(rows, cols)

    # Start the game
    print("Welcome to the game! Markings: A - Start, B - Stop, @ - Your position, X - Obstacle, Q or q - exit the game")
    move(board, start, stop)


if __name__ == "__main__":
    start_game(rows, cols)

