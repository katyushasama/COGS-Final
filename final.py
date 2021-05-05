import time
import copy
import sys
'''
This Project is a project using minimax algogrithm to run tic-tac-toe
Minimax Algorithm is a DFS algorithm
reference:
https://en.wikipedia.org/wiki/Minimax
https://github.com/CodingTrain/website/tree/main/CodingChallenges/CC_154_Tic_Tac_Toe_Minimax/P5
The basic idea of the minimax algorithm is from this website and the wikipidia
'''
def draw(l):
	#This is the print function, the use of this
	#function is to draw the grid out.
	print( '   1  2  3')
	temp = ''
	for i in range(len(l)):
		if i == 0:
			temp += 'A: '
		elif i == 1:
			temp+= 'B: '
		else:
			temp+= 'C: '
		for j in range(len(l[i])):
			temp += str(l[i][j])
			temp += ' '
			if j < 2:
				temp += '|'
		print(temp)
		temp = ''
		if i < 2:
			print('   --------')

def check_win(grid):
	'''
	This function is to check is there a winner appeal
	it will check diagonal, horizontal, vertical of the gird
	'''
	if grid[0][0] != " " and (grid[0][0] == grid[0][1] == grid[0][2]):
		return grid[0][0]
	elif grid[1][0] != " " and (grid[1][0] == grid[1][1] == grid[1][2]):
		return grid[1][0]
	elif grid[2][0] != " " and  (grid[2][0] == grid[2][1] == grid[2][2]):
		return grid[2][0]
	elif grid[0][0] != " " and  (grid[0][0] == grid[1][0] == grid[2][0]):
		return grid[0][0]
	elif grid[0][1] != " " and (grid[0][1] == grid[1][1] == grid[2][1]):
		return grid[0][1]
	elif grid[0][2] != " " and  (grid[0][2] == grid[1][2] == grid[2][2]):
		return grid[0][2]
	elif grid[0][0] != " " and  (grid[0][0] == grid[1][1] == grid[2][2]):
		return grid[0][0]
	elif grid[0][2] != " " and  (grid[0][2] == grid[1][1] == grid[2][0]):
		return grid[0][2]
	else:
		count = 0
		for i in grid:
			for j in i:
				if j == " ":
					count += 1
		if count == 0:
			return "Tie"
		else:
			return None

def check_move(grid):
	'''
	This is the chech move function
	this function will use the recursion fucntion call DFS_minimax
	to calculate the best move for AI
	and return the best move
	'''
	best_score = -(float("inf"))
	points = (None,None)
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == " ":
				temp_grid = copy.deepcopy(grid)
				temp_grid[i][j] = "O"
				temp_score = DFS_minimax(temp_grid,False)
				#print(temp_score)
				if best_score < temp_score:
					best_score = temp_score
					points = (i,j)
	return points


def DFS_minimax(grid,AI):
	'''
	This is the minimax recursion function
	It is a like-BFS function
	It will check all the possible moves and calculate the score
	and return the highest score for AI to determine where to go
	'''
	if check_win(grid) != None:
		win_or_not = check_win(grid)
		if win_or_not == "X":
			return -1
		elif win_or_not == "O":
			return 1
		elif win_or_not == "Tie":
			return 0
	if AI:
		best_score = -40360
		#do not have to be -inf,
		# the worst case of the algorithm is 8! = 40360 
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if grid[i][j] == " ":
					grid[i][j] = "O"
					temp_score = DFS_minimax(grid,False)
					grid[i][j] = " "
					best_score = max(temp_score,best_score)
		return best_score
	else:
		best_score = 40360
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if grid[i][j] == " ":
					grid[i][j] = "X"
					temp_score = DFS_minimax(grid,True)
					grid[i][j] = " "
					best_score = min(temp_score,best_score)
		return best_score


def play():
	grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
	steps = 0
	flag = True
	print("Here is the game,AI will go first, Try to beat AI")
	while True:
		if flag == True:
			print("AI Turn")
			check_grid = copy.deepcopy(grid)
			sth = check_move(check_grid)
			grid[sth[0]][sth[1]] = "O"
			draw(grid)
			check = check_win(grid)
			if check != None:
				return check
		print('Please type in the location you would like to go')
		print('if you do not want to play, type "quit"')
		inp = input('For example go to A1 type A1 =>')
		if inp == "quit":
			return 'quit'
		inp = inp.strip()
		inp = list(inp)
		#print(inp)
		if len(inp) != 2:
			print('INVAILD INPUT, Please try again')
			flag = False
			continue
		if inp[0] not in ['A','B','C'] or int(inp[1]) > 3:
			print('INVAILD INPUT, Please try again')
			flag = False
			continue
		temp = 0
		if inp[0] == 'A':
			temp =0
		elif inp[0] == 'B':
			temp = 1
		else:
			temp = 2
		if grid[temp][int(inp[1])-1] != ' ':
			print('some piece already been place here, try another place')
			flag = False
			continue
		else:
			grid[temp][int(inp[1])-1] = 'X'
			flag = True
			if check != None:
				return check
		draw(grid)
def main():
	while True:
		a = play()
		if a != 'quit':
			if a != "Tie":
				print("{} Win".format(a))
			else:
				print("Tie")
			print("game over")
			inp = input("do you want to play again ?(if yes type yes, else type no)")
			if inp == "yes":
				continue
			else:
				break
		else:
			break
main()
