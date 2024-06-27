import math

# Constants
HUMAN = -1
AI = +1
EMPTY = 0

def print_board(board):
    """Print the board."""
    chars = {HUMAN: 'X', AI: 'O', EMPTY: ' '}
    for row in board:
        print("|".join(chars[cell] for cell in row))
        print("-" * 5)

def check_winner(board):
    """Check if there is a winner."""
    winning_positions = [
        [(0, 0), (0, 1), (0, 2)],  # Rows
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],  # Columns
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],  # Diagonals
        [(0, 2), (1, 1), (2, 0)]
    ]

    for positions in winning_positions:
        values = [board[x][y] for x, y in positions]
        if values == [AI, AI, AI]:
            return AI
        if values == [HUMAN, HUMAN, HUMAN]:
            return HUMAN
    return EMPTY

def game_over(board):
    """Check if the game is over."""
    return check_winner(board) != EMPTY or all(cell != EMPTY for row in board for cell in row)

def get_empty_cells(board):
    """Return a list of empty cells."""
    return [(x, y) for x in range(3) for y in range(3) if board[x][y] == EMPTY]

def minimax(board, depth, player):
    """Minimax algorithm."""
    if player == AI:
        best = [-1, -1, -math.inf]
    else:
        best = [-1, -1, math.inf]

    if game_over(board):
        score = check_winner(board)
        return [-1, -1, score]

    for cell in get_empty_cells(board):
        x, y = cell
        board[x][y] = player
        score = minimax(board, depth + 1, -player)
        board[x][y] = EMPTY
        score[0], score[1] = x, y

        if player == AI:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best

def ai_turn(board):
    """AI turn."""
    if len(get_empty_cells(board)) == 9:
        x, y = 1, 1
    else:
        move = minimax(board, 0, AI)
        x, y = move[0], move[1]
    board[x][y] = AI

def human_turn(board, x, y):
    """Human turn."""
    if board[x][y] == EMPTY:
        board[x][y] = HUMAN
        return True
    return False

def play():
    """Main function to play the game."""
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print_board(board)

    while not game_over(board):
        x, y = map(int, input("Enter your move (row and column): ").split())
        if human_turn(board, x, y):
            print_board(board)
            if game_over(board):
                break
            ai_turn(board)
            print_board(board)

    winner = check_winner(board)
    if winner == HUMAN:
        print("You win!")
    elif winner == AI:
        print("AI wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play()
