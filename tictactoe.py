"""
Tic Tac Toe Player
"""

import math
import copy #this is so we an create a deep copy of the game board

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
	tot_x = 0
	tot_o = 0
	for row in board:
		tot_x += row.count(X)
		tot_o +=row.count(O)

	if tot_x > tot_o:
		return O
	else:
		return X
	#NOTE!: I deleted 'raise NotImplementedError' here as I don't think it is needed (think it is a placeholder), but not 100% sure atm


def actions(board):
	"""
	Returns set of all possible actions (i, j) available on the board.
	"""
	if isinstance(board,list):
		pass
	else:
		raise TypeError("Please input correct format for a board") 
	if len(board) != 3:
		raise ValueError("The board should have 3 rows, so it's list should have length 3") #not sure if these are right type of errors

	possibles = set()
	for row in range(3):        #note here that i denotes the row of board and j denotes the column
		for column in range(3):
			if board[row][column] == None:
				possibles.add((row,column))  #This may not work - it might literally add (i,j) to the set, not what i and j denote

	return possibles


	
def result(board, action):
	"""
	Returns the board that results from making move (i, j) on the board.
	"""
	if board[action[0]][action[1]] != EMPTY:
		raise Exception("This space has already been taken - please choose another")

	og = copy.deepcopy(board)

	og[action[0]][action[1]] = player(board) 
	return og




def winner(board):
	global winner
	for mark in [X,O]:
		if board[0][0]==board[0][1]==board[0][2]== mark or board[1][0]==board[1][1]==board[1][2]==mark  or \
		board[2][0]==board[2][1]==board[2][2]== mark or board[0][0]==board[1][0]==board[2][0]== mark or \
		board[0][1]==board[1][1]==board[2][1]== mark or board[0][2]==board[1][2]==board[2][2]== mark or \
		board[0][0]==board[1][1]==board[2][2]==mark or board [0][2]==board[1][1]==board[2][0]==mark:
			return mark
		#this function will automatically return 'None' if there is no winner


def terminal(board):
	"""
	Returns True if game is over, False otherwise.
	"""
	if winner(board) == X or winner(board) == O:
		return True
	elif board[0][0]!=None and board[0][1]!=None and board[0][2]!=None and board[1][0]!=None and board[1][1]!=None and \
	board[1][2]!=None and board[2][0]!=None and board[2][1]!=None and board[2][2]!=None:
		return True
	else:
		return False


def utility(board):
	"""
	Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
	"""
	if winner(board) == X:
		return 1
	elif winner(board) == O:
		return -1
	else:
		return 0




def minimax(board):
	if player(board) == X:
		return maxval(board)[1]
	else:
		return minval(board)[1]


def maxval(board):
	if terminal(board):
		return [utility(board),None]
	else:
		bestmove = None
		v = -20
		for possible in actions(board):
			if minval(result(board,possible))[0] > v:
				v = minval(result(board,possible))[0]
				bestmove = possible

		return [v, bestmove]


def minval(board):
	if terminal(board):
		return [utility(board),None]
	else:
		bestmove = None
		v = 20
		for possible in actions(board):
			if maxval(result(board,possible))[0] < v:
				v = maxval(result(board,possible))[0]
				bestmove = possible

		return [v, bestmove]



#print(minimax(initial_state()))
#print(minimax([[X,O,X],[EMPTY,O,EMPTY],[X,EMPTY,O]]))

print(minimax([[X,X,O],[O,X,EMPTY],[EMPTY,O,EMPTY]]))
