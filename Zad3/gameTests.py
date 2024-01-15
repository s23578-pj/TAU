import unittest
from io import StringIO
from unittest.mock import patch
from Zad3.Game import generate_board, display_board, number_of_obstacles, rows, cols, make_move


class MyTestGameFunctions(unittest.TestCase):

    def test_generate_board_size(self):
        board, start, stop = generate_board(rows, cols)
        self.assertEqual(rows, len(board))
        self.assertEqual(cols, len(board[0]))

    def test_start_on_border(self):
        board, start, stop = generate_board(rows, cols)
        start_row, start_col = start
        self.assertTrue(start_row == 0 or start_row == rows - 1 or
                        start_col == 0 or start_col == cols - 1)

    def test_stop_on_border(self):
        board, start, stop = generate_board(rows, cols)
        end_row, end_col = stop
        self.assertTrue(end_row == 0 or end_row == rows - 1 or
                        end_col == 0 or end_col == cols - 1)

    def test_obstacle_detection(self):
        board, start, stop = generate_board(rows, cols)
        player_row, player_col = start
        board[player_row][player_col] = '_'
        board[player_row - 1][player_col] = 'X'
        new_row, new_col = make_move(board, start, 'W')
        self.assertEqual(new_row, player_row)
        self.assertEqual(new_col, player_col)

    def test_amount_of_obstacles(self):
        board, start, stop = generate_board(rows, cols)
        obstacles_count = sum(row.count('X') for row in board)
        self.assertEqual(obstacles_count, number_of_obstacles)

    def test_movement_up(self):
        while True:
            board, start, _ = generate_board(rows, cols)
            board[start[0]][start[1]] = '_'

            if start[0] > 0 and board[start[0] - 1][start[1]] != 'X':
                new_row, new_col = make_move(board, start, 'W')
                self.assertEqual(new_row, start[0] - 1)
                self.assertEqual(new_col, start[1])
                break

    def test_movement_down(self):
        while True:
            board, start, _ = generate_board(rows, cols)
            board[start[0]][start[1]] = '_'

            if start[0] < rows - 1 and board[start[0] + 1][start[1]] != 'X':
                new_row, new_col = make_move(board, start, 'S')
                self.assertEqual(new_row, start[0] + 1)
                self.assertEqual(new_col, start[1])
                break

    def test_movement_left(self):
        while True:
            board, start, _ = generate_board(rows, cols)
            board[start[0]][start[1]] = '_'

            if start[1] > 0 and board[start[0]][start[1] - 1] != 'X':
                new_row, new_col = make_move(board, start, 'A')
                self.assertEqual(new_row, start[0])
                self.assertEqual(new_col, start[1] - 1)
                break

    def test_movement_right(self):
        while True:
            board, start, _ = generate_board(rows, cols)
            board[start[0]][start[1]] = '_'

            if start[1] < cols - 1 and board[start[0]][start[1] + 1] != 'X':
                new_row, new_col = make_move(board, start, 'D')
                self.assertEqual(new_row, start[0])
                self.assertEqual(new_col, start[1] + 1)
                break

    def test_invalid_movement(self):
        board, start, stop = generate_board(rows, cols)
        player_row, player_col = start
        board[player_row][player_col] = '_'
        new_row, new_col = make_move(board, start, 'Z')
        self.assertEqual(new_row, player_row)
        self.assertEqual(new_col, player_col)

    def test_print_board(self):
        board, start, stop = generate_board(rows, cols)
        current_position = start
        with patch('sys.stdout', new=StringIO()) as fake_output:
            display_board(board, current_position)
            printed_board = fake_output.getvalue().strip()
        self.assertIsInstance(printed_board, str)

        print("\n\n" + printed_board)
