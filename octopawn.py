import json

tt = {}

def octopawn():
    # Define your initial state
    initial_state = ("pppp.........PPPP", 'W')
    
    # Run the negamax algorithm from the initial state
    negamax(initial_state)
    # Save the transposition table to a JSON file
    save_to_json()

def negamax(s):
    print(s)
    if s in tt:
        return tt[s]
    
    board, side = s

    # Check if the current state is a win for the opponent
    if is_win_for_opponent(board, side):
        tt[s] = -1
        return -1

    # Get legal moves for the current state
    ms = legal_moves(board, side)

    v = None
    for m in ms:
        b = make_move(board, m)
        r = -negamax((b, opponent(side)))

        if v is None or r > v:
            v = r
    if v == -1:
        tt[s] = v
    return v

# Function to check if the current state is a win for the opponent
def is_win_for_opponent(board, side):
    if legal_moves(board, side) == []:
        return True
    
    if side == 'B':
        for i in range(0, 3):
            if (board[i] == 'P'):
                return True

    elif side == 'W':
        for i in range(12, 15):
            if (board[i] == 'p'):
                return True
    return False

# Function to get legal moves for the current state
def legal_moves(board, side):
    moves = []
    if side == 'B':
        v = 'p'
        for i in range(len(board)):
            if board[i] == v:
                # Check if the pawn can move forward
                if i + 4 < len(board) and board[i + 4] == '.':
                    s = list(board)
                    s[i] = '.'
                    s[i+4] = v
                    moves.append(''.join(s))
                # Check if the pawn can capture diagonally to the right
                if i + 5 < len(board) and board[i + 5] == opponent(side):
                    s = list(board)
                    s[i] = '.'
                    s[i+5] = v
                    moves.append(''.join(s))
                # Check if the pawn can capture diagonally to the left
                if i + 3 >= 0 and board[i + 3] == opponent(side):
                    s = list(board)
                    s[i] = '.'
                    s[i+3] = v
                    moves.append(''.join(s)) 
    else:
        v = 'P'
        for i in range(len(board)):
            if board[i] == v:
                # Check if the pawn can move forward
                if i - 4 < len(board) and board[i - 4] == '.':
                    s = list(board)
                    s[i] = '.'
                    s[i-4] = v
                    moves.append(''.join(s)) 
                # Check if the pawn can capture diagonally to the right
                if i - 3 < len(board) and board[i - 3] == opponent(side):
                    s = list(board)
                    s[i] = '.'
                    s[i-3] = v
                    moves.append(''.join(s))
                # Check if the pawn can capture diagonally to the left
                if i - 5 >= 0 and board[i - 5] == opponent(side):
                    s = list(board)
                    s[i] = '.'
                    s[i-5] = v
                    moves.append(''.join(s))

    return moves


# Function to make a move on the board
def make_move(board, move):
    return move

# Function to get the opponent's side
def opponent(side):
    return 'W' if side == 'B' else 'B'

# Save the transposition table to a JSON file
def save_to_json():
    tt_str_keys = {str(key): value for key, value in tt.items()}
    
    with open('4pawn.json', 'w') as json_file:
        json.dump(tt_str_keys, json_file, indent = 1)
# Run the Octopawn algorithm
octopawn()
