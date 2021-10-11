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


suk = Sudoku()

suk.sudoku_board[0][0][0] = 9
suk.sudoku_board[1][1][1] = 9
suk.sudoku_board[0][2][2] = 5
suk.sudoku_board[1][2][0] = 4
suk.sudoku_board[3][1][2] = 6
suk.sudoku_board[4][1][0] = 7
suk.sudoku_board[8][2][2] = 2
suk.sudoku_board[7][2][0] = 1


suk.printer()

print(suk.checker())
