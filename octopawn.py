import json

tt = {}

def octopawn():

    initial_state = ("pppp.........PPPP", 'W')
    

    negamax(initial_state)
    
    save_to_json()

def negamax(s):
  #  print(s)
    if s in tt:
        return tt[s]
    
    board, side = s

    if is_win_for_opponent(board, side):
        tt[s] = -1
        return -1

    ms = legal_moves(board, side)
    if ms == []:
        tt[s] = -1
        return -1

    v = None
    for m in ms:
        b = m
        r = -negamax((b, opponent(side)))

        if v is None or r > v:
            v = r
            
    tt[s] = v
    return v


def is_win_for_opponent(board, side):
   # if legal_moves(board, side) == []:
   #     return True
    
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
                if i + 5 < len(board) and board[i + 5] == opponent(side) and i not in (3, 7, 11):
                    s = list(board)
                    s[i] = '.'
                    s[i+5] = v
                    moves.append(''.join(s))
                # Check if the pawn can capture diagonally to the left
                if i + 3 >= 0 and board[i + 3] == opponent(side) and i + 3 < len(board) and i not in (0, 4, 8, 12):
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
                if i - 3 < len(board) and board[i - 3] == opponent(side) and i not in (3, 7, 11, 15):
                    s = list(board)
                    s[i] = '.'
                    s[i-3] = v
                    moves.append(''.join(s))
                # Check if the pawn can capture diagonally to the left
                if i - 5 >= 0 and board[i - 5] == opponent(side) and i not in (12, 8, 4, 0):
                    s = list(board)
                    s[i] = '.'
                    s[i-5] = v
                    moves.append(''.join(s))

   # print(moves)

    return moves



def make_move(board, move):
    return move


def opponent(side):
    return 'W' if side == 'B' else 'B'


def save_to_json():
    tt_str_keys = {','.join(key): value for key, value in tt.items()}

    with open('4pawn.json', 'w') as json_file:
        json.dump(tt_str_keys, json_file, indent=1, sort_keys=True)



octopawn()
