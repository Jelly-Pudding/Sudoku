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
		#Checks horizontal
		for number in range(1, 10, 1):
			for row in range(0, 9, 1):
				count_numbers = [row.count(number) for row in suk.sudoku_board[row]]
				summed = sum(count_numbers)
				if summed > 1:
					return False
		#Checks vertical
		two_d_list = []
		for e1 in suk.sudoku_board:
			for e2 in e1:
				two_d_list.append(e2)
		one_d_list = []
		for e1 in two_d_list:
			for e2 in e1:
                		one_d_list.append(e2)
		for i in range(9):
			spliced_list = one_d_list[i:]
			every_other_element = spliced_list[::9]
			for numbers in range(1, 10, 1):	
				counted = every_other_element.count(numbers)
				if counted >1:
					return False

suk = Sudoku()

suk.sudoku_board[8][2][2] = 1
suk.sudoku_board[7][2][2] = 1
suk.printer()


print(suk.checker())
