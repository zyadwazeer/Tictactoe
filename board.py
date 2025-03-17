def initialize_boards():
    """Creates an empty 3x3 Tic Tac Toe board."""
    boards = []
    for i in range(3):
        boards.append(["-", "-", "-"])
    return boards

def print_board(board):
    """Prints the game board."""
    print("Current game board:")
    for row in board:
        print(" | ".join(row))
    print()