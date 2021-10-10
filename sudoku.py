class Sudoku:
	def __init__(self):
		self.sudoku_board = [[[0 for row in range(3)] for column in range(3)] for expandboard in range(9)]
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

suk = Sudoku()

suk.sudoku_board[0][0][0] = 0
print(" ")
suk.sudoku_board[1][0][0] = 1
suk.sudoku_board[2][0][0] = 2
suk.sudoku_board[3][0][0] = 3
suk.sudoku_board[4][0][0] = 4
suk.sudoku_board[5][0][0] = 5
suk.sudoku_board[6][0][0] = 6
suk.sudoku_board[7][0][0] = 7
suk.sudoku_board[8][0][0] = 8

suk.sudoku_board[1][1][0] = 1
suk.sudoku_board[2][1][0] = 2
suk.sudoku_board[3][1][0] = 3
suk.sudoku_board[4][1][0] = 4
suk.sudoku_board[5][1][0] = 5
suk.sudoku_board[6][1][0] = 6
suk.sudoku_board[7][1][0] = 7
suk.sudoku_board[8][1][0] = 8

suk.sudoku_board[1][2][2] = 1
suk.sudoku_board[2][2][2] = 2
suk.sudoku_board[3][2][2] = 3
suk.sudoku_board[4][2][2] = 4
suk.sudoku_board[5][2][2] = 5
suk.sudoku_board[6][2][2] = 6
suk.sudoku_board[7][2][2] = 7
suk.sudoku_board[8][2][2] = 8


suk.printer()


