import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    # Checking diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def get_ai_move(board):
    # Try to win
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                if check_winner(board):
                    return row, col
                board[row][col] = ' '

    # Try to block the player from winning
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                if check_winner(board):
                    board[row][col] = 'O'
                    return row, col
                board[row][col] = ' '

    # Make a random move
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col


def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print()

        if current_player == 'X':
            while True:
                row = int(input("Player X, enter row (1-3): ")) - 1
                col = int(input("Player X, enter column (1-3): ")) - 1
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                    break
                else:
                    print("Invalid move. Try again.")
        else:  # AI's turn
            row, col = get_ai_move(board)

        board[row][col] = current_player  # Board Updation

        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # For switching players
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_tic_tac_toe()
