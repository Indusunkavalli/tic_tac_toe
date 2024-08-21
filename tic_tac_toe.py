mport math

# Constants
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2

def print_board(board):
    symbols = {EMPTY: ' ', PLAYER_X: 'X', PLAYER_O: 'O'}
    for i in range(3):
        print(" | ".join(symbols[board[i * 3 + j]] for j in range(3)))
        if i < 2:
            print("---------")

def check_win(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def check_draw(board):
    return all(cell != EMPTY for cell in board)

def evaluate_board(board):
    if check_win(board, PLAYER_X):
        return 10
    if check_win(board, PLAYER_O):
        return -10
    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate_board(board)
    
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if check_draw(board):
        return 0
    
    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                best = max(best, minimax(board, depth + 1, False))
                board[i] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                best = min(best, minimax(board, depth + 1, True))
                board[i] = EMPTY
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_X
            move_val = minimax(board, 0, False)
            board[i] = EMPTY
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_move

def play_game():
    board = [EMPTY] * 9
    current_player = PLAYER_X
    
    while True:
        print_board(board)
        
        if current_player == PLAYER_X:
            move = find_best_move(board)
        else:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8:
                print("Invalid move. Try again.")
                continue

        if board[move] != EMPTY:
            print("Invalid move. Try again.")
            continue
        
        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            if current_player == PLAYER_X:
                print("AI wins!")
            else:
                print("You win!")
            return
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            return
        
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

if _name_ == "_main_":
    play_game()