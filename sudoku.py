import numpy as np

class Sudoku:
	def __init__(self):
		self.sudoku_board = [[[0 for item_in_box_row in range(3)] for box_per_box_row in range(3)] for horizontal_line in range(9)]
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

	def checker(self):

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

suk = Sudoku()

suk.sudoku_board[0][0][0] = 1
suk.sudoku_board[1][2][2] = 1
suk.sudoku_board[2][2][2] = 1

suk.printer()


print(suk.checker())
