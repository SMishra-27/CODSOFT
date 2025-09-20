# Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. You can use algorithms like Minimax with
 or without Alpha-Beta Pruning to make the AI player unbeatable.
 This project will help you understand game theory and basic search
 algorithms
import math

# Initialize board
board = [" " for _ in range(9)]

# Print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

# Check for winner
def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check if board is full
def is_full(board):
    return " " not in board

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, "O"):
        return 10 - depth
    elif check_winner(board, "X"):
        return depth - 10
    elif is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth+1, alpha, beta, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth+1, alpha, beta, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# AI move
def best_move(board):
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Game loop
def play_game():
    print("Tic-Tac-Toe: You are X, AI is O")
    print_board(board)

    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue
        board[move] = "X"

        print_board(board)

        if check_winner(board, "X"):
            print("You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        # AI move
        best_move(board)
        print("AI played:")
        print_board(board)

        if check_winner(board, "O"):
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

play_game()
