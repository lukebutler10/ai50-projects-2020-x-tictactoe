
from XnO import actions

X = "X"
O = "O"
EMPTY = None



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board.count("X") > board.count("O"):
        player = O
    else:
        player = X

    print("Player {} has the next next turn".format(player))

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibles = set()
    for i in range(3):        #note here that i denotes the row of board and j denotes the column
        for j in range(3):
            if board[i][j] == None:
                possibles.add((i,j))  #THis may not work - it might literally add (i,j) to the set, not what i and j denote

    print(possibles)


    raise TypeError("Please input correct format for a board") #find out if this is ok, or if I should remove it/add more errors


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action #.....TO DO: create error message if action not correctly inputted by user

    og = copy.deepcopy(board)

    row = action[0]
    column = action[1]

    board[action[0]][action[1]] == player




    raise NotImplementedError

#original winner code:
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    global winner

    if board[0][0]==board[0][1]==board[0][2]== X or board[1][0]==board[1][1]==board[1][2]== X or board[2][0]==board[2][1]==board[2][2]== X or \
    board[0][0]==board[1][0]==board[2][0]== X or board[0][1]==board[1][1]==board[2][1]== X or board[0][2]==board[1][2]==board[2][2]== X or \
    board[0][0]==board[1][1]==board[2][2]==X or board [0][2]==board[1][1]==board[2][0]==X:
        winner = X
        return "X wins"
        
    elif board[0][0]==board[0][1]==board[0][2]== O or board[1][0]==board[1][1]==board[1][2]== O or board[2][0]==board[2][1]==board[2][2]== O or \
    board[0][0]==board[1][0]==board[2][0]== O or board[0][1]==board[1][1]==board[2][1]== O or board[0][2]==board[1][2]==board[2][2]== O or \
    board[0][0]==board[1][1]==board[2][2]==O or board [0][2]==board[1][1]==board[2][0]==O:
        winner = O
        return "O wins"

    else:
        winner = None




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    bestscore = -10
    bestmove = None
    for possible in actions(board):
        result(board,possible)
        if playerturn == X:
            score = alg(ismax == True, result(board,possible))
        else:
            score = alg(ismax == False, result(board,possible))
        if score > bestscore:
            bestscore = score
            bestmove = possible

    return bestmove


def alg(ismax, board):
        if utility(result(board,possible)) != 0:
            return utility(result(board,possible))
        elif terminal(result(board,possible)) == True:
            return 0

        scores_dict = []
        for possible in actions(board):
            scores.append(alg(not ismax,result(board, possible)))

        return max(scores) if ismax else min(scores)

#change these last few lines so that scores is a dictionarty or smething
#similar where you can have a 'score' and 'possible' pair, and so that
#after I can call the max score and return its corresponding [ossible
#ie the action that goes with it



def move(board):
        if utility(result(board,possible)) != 0:
            value =  utility(result(board,possible))
            return value
        elif terminal(result(board,possible)) == True:
            value = 0
            return value
        else:
            value = move(result(board, possible))
            return (possible, value)




##THIS WAS WHAT I WAS TRYING BEFORE I REALISED HOW SIMPLE THE SOLUTION WAS, AND THAT HE BASICALLY GAVE IT TO US IN THE LECTURE:
ismax=False

def alg(ismax, board):

        if terminal(board):
            return utility(board)

        else:
            scores = []
            for possible in actions(board):
                scores.append(alg(not ismax,result(board, possible)))

            return max(scores) if ismax else min(scores)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    bestmove = None
    for possible in actions(board):
        
        if player(board) == X:
            score = alg(ismax == True, result(board,possible))
            bestscore = -10
            if score > bestscore:
                bestscore = score
                bestmove = possible
        else:
            score = alg(ismax == False, result(board,possible))
            bestscore = 10
            if score < bestscore:
                bestscore = score
                bestmove = possible
            
    return bestmove



'''
def minimax(board):
    if player(board) == X:
        return maxval(board)
    else:
        return minval(board)


def maxval(board):
    if terminal(board):
        return utility(board)
    else:
        bestmove = None
        v = -20
        for possible in actions(board):
            if minval(result(board,possible)) > v:
                v = minval(result(board,possible))
                bestmove = possible

        return bestmove


def minval(board):
    if terminal(board):
        return utility(board)
    else:
        bestmove = None
        v = 20
        for possible in actions(board):
            if maxval(result(board,possible)) < v:
                v = maxval(result(board,possible))
                bestmove = possible

        return bestmove
'''






















