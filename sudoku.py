import copy
class Sudoku:
	def __init__(self):
		self.sudoku_board = [[[0 for item_in_box_rows in range(3)] for box_per_row_of_boxes in range(3)] for horizontal_line in range(9)]
	def printer(self):
		count = 0
		print("=========================")
		for i, block in enumerate(self.sudoku_board):
			count += 1
			stringer = " ".join(str(item) for item in block)
			stringer = stringer.replace("[","| ") + " |"
			stringer = stringer.replace("]","")
			stringer = stringer.replace(",","")
			print(stringer)
			if count % 3 == 0:
				print("=========================")									

	def next_available_move(self):
		#goes left to right, top to bottom
		for i in range(0, 9, 1):
			for j in range(0, 3, 1):
				for k in range(0, 3, 1):
					if self.sudoku_board[i][j][k] == 0:
						return [i, j, k]
		#returns False if there are no possible moves
		return False

	def checker(self):
		skip_list = False
		number = 0
		#conversion to 2d list then 1d list for easier checking

		two_d_list = []
		for e1 in self.sudoku_board:
			for e2 in e1:
				two_d_list.append(e2)
		one_d_list = []
		for e1 in two_d_list:
			for e2 in e1:
                		one_d_list.append(e2)

		#horizontal checker

		for i in range(9, 82, 9):
			sliced_list = one_d_list[i - 9:i]
			for numbers in range(1, 10, 1):
				counted = sliced_list.count(numbers)
				if counted >1:
					return False

		#vertical checker
		
		for i in range(9):
			spliced_list = one_d_list[i:]
			every_other_element = spliced_list[::9]
			for numbers in range(1, 10, 1):	
				counted = every_other_element.count(numbers)
				if counted >1:
					return False

		#box checker

		for i in range(0, 28, 3):
			if i == 9:
				skip_list = True
				number += 15
			elif i == 18:
				number += 18
				sliced_list = one_d_list[33:33+27]
			elif skip_list == True:
				sliced_list = one_d_list[i+number:i+number+27]
			else:
				sliced_list = one_d_list[i:i+27]
			first_three = sliced_list[0:3]
			second_three = sliced_list[9:12]
			third_three = sliced_list[18:21]
			all_elements = first_three + second_three + third_three
			for numbers in range(1, 10, 1):
				counted = all_elements.count(numbers)
				if counted >1:
					return False

		#the position must be valid if false has not been returned yet

		return True
		
suk = Sudoku()

suk.sudoku_board[1][0][0] = 5
suk.sudoku_board[2][0][0] = 3
suk.sudoku_board[4][0][0] = 8
suk.sudoku_board[7][0][0] = 2
suk.sudoku_board[2][0][1] = 8
suk.sudoku_board[4][0][1] = 4
suk.sudoku_board[7][0][1] = 7
suk.sudoku_board[3][0][2] = 6
suk.sudoku_board[5][0][2] = 5
suk.sudoku_board[6][0][2] = 4
suk.sudoku_board[2][1][0] = 7
suk.sudoku_board[3][1][0] = 4
suk.sudoku_board[7][1][0] = 3
suk.sudoku_board[0][1][1] = 2
suk.sudoku_board[4][1][2] = 3
suk.sudoku_board[8][1][2] = 9
suk.sudoku_board[0][2][0] = 6
suk.sudoku_board[4][2][0] = 9
suk.sudoku_board[8][2][1] = 1
suk.sudoku_board[2][2][2] = 2
suk.sudoku_board[5][2][2] = 8
suk.sudoku_board[7][2][2] = 6

def backtracking(classer):
	#a recursive function for finding a solution - it is very quick because it checks if the current board configuration is valid, and if it isn't it goes back a step (backtracking)
	if classer.next_available_move() == False:
		#means there are no moves left - i.e. the solution has been found
		return True
	else:
		#gets the next available move as a list of indices
		move_index = classer.next_available_move()
		#makes a copy - ensuring invalid moves aren't immediately fed into the main board
		copied = copy.deepcopy(classer)
		for i in range(1, 10, 1):
			copied.sudoku_board[move_index[0]][move_index[1]][move_index[2]] = i
			if copied.checker() == True:
				classer.sudoku_board[move_index[0]][move_index[1]][move_index[2]] = i
				classer.printer()
				#The recursive part of the function (function called inside itself) 
				if backtracking(classer) == True:
					return True
			#Goes back a step (backtracks) and blanks the tile as the current board configuration must be invalid (move is invalid or it does not solve the puzzle)
			classer.sudoku_board[move_index[0]][move_index[1]][move_index[2]] = 0
		#returns False as there's no solution if the function gets to this line without returning yet
		return False
					
#backtracking(suk)
#suk.printer()







