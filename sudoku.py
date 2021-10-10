class Sudoku:
	def __init__(self):
		self.sudoku_board = [[[0 for item_in_box_row in range(3)] for box_per_box_row in range(3)] for horizontal_line in range(9)]
	def printer(self):
		count = 0
		print("_________________________\n")
		for i, block in enumerate(self.sudoku_board):
			count += 1
			if count % 3 == 0:
				stringer = " ".join(str(item) for item in block)
				stringer = stringer.replace("[","| ") + " |"
				stringer = stringer.replace("]","")
				stringer = stringer.replace(",","")
				print(stringer)	
				print("_________________________")
			else:
				stringer = " ".join(str(item) for item in block)
				stringer = stringer.replace("[","| ") + " |"
				stringer = stringer.replace("]","")
				stringer = stringer.replace(",","")
				print(stringer)								
			print() 
	def checker(self):
		#Checks horizontal
		for number in range(1, 10, 1):
			for row in range(0, 9, 1):
				count_numbers = [row.count(number) for row in suk.sudoku_board[row]]
				summed = sum(count_numbers)
				if summed > 1:
					return False


suk = Sudoku()


suk.sudoku_board[0][1][1] = 1
suk.sudoku_board[5][1][1] = 5
suk.sudoku_board[7][1][1] = 5
suk.sudoku_board[6][1][1] = 5
suk.sudoku_board[8][1][1] = 5
suk.sudoku_board[2][1][1] = 5
suk.sudoku_board[3][1][1] = 5
suk.sudoku_board[1][1][1] = 5
suk.sudoku_board[0][2][2] = 1


suk.printer()

print(suk.checker())
