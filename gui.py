import copy
import numpy as np
import pygame, sys
from sudoku import Sudoku

bot = Sudoku()

bot.sudoku_board[1][0][0] = 5
bot.sudoku_board[2][0][0] = 3
bot.sudoku_board[4][0][0] = 8
bot.sudoku_board[7][0][0] = 2
bot.sudoku_board[2][0][1] = 8
bot.sudoku_board[4][0][1] = 4
bot.sudoku_board[7][0][1] = 7
bot.sudoku_board[3][0][2] = 6
bot.sudoku_board[5][0][2] = 5
bot.sudoku_board[6][0][2] = 4
bot.sudoku_board[2][1][0] = 7
bot.sudoku_board[3][1][0] = 4
bot.sudoku_board[7][1][0] = 3
bot.sudoku_board[0][1][1] = 2
bot.sudoku_board[4][1][2] = 3
bot.sudoku_board[8][1][2] = 9
bot.sudoku_board[0][2][0] = 6
bot.sudoku_board[4][2][0] = 9
bot.sudoku_board[8][2][1] = 1
bot.sudoku_board[2][2][2] = 2
bot.sudoku_board[5][2][2] = 8
bot.sudoku_board[7][2][2] = 6

class Pane(object):
	def __init__(self):
		pygame.init()
		self.font = pygame.font.SysFont("Arial", 17)
		pygame.display.set_caption("Sudoku")	
		self.screen = pygame.display.set_mode((225, 225), 0, 32)
		self.screen.fill((255, 255, 255))
		pygame.display.update()
		self.FPS = 60
	def add_rectangle(self):
		count = -1
		#tranposes the 3d list so when it is converted to 1d, it fills in the board correctly as this function fills in numbers in a different order
		newlist = np.transpose(bot.sudoku_board, axes=(1, 2, 0)).tolist()
		two_d_list = []
		for e1 in newlist:
			for e2 in e1:
				two_d_list.append(e2)
		one_d_list = []
		for e1 in two_d_list:
			for e2 in e1:
				one_d_list.append(e2)

		for i in range(0, 9, 1):
			for j in range(0, 9, 1):
				count +=1		
				self.rect = pygame.draw.rect(self.screen, ((0, 0, 0)), (i*25, j*25, 25, 25), 1)
				if one_d_list[count] == 0:				
					self.screen.blit(self.font.render(" ", True, (255, 0, 0)), (i*25+7, j*25+2))
				elif one_d_list[count] != 0:
					self.screen.blit(self.font.render(str(one_d_list[count]), True, (0, 140, 140)), (i*25+7, j*25+2)) 				
				
		self.line = pygame.draw.line(self.screen, ((0, 0, 0)), (75, 0), (75, 225), 4)
		self.line = pygame.draw.line(self.screen, ((0, 0, 0)), (150, 0), (150, 225), 4)
		self.line = pygame.draw.line(self.screen, ((0, 0, 0)), (0, 75), (225, 75), 4)
		self.line = pygame.draw.line(self.screen, ((0, 0, 0)), (0, 150), (225, 150), 4)
		
		pygame.display.update()
		

	def backtracking(self, classer):
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
					#blanks the screen so numbers don't overlap one another
					self.screen.fill((255, 255, 255))
					#updates the screen with the new numbers
					self.add_rectangle()
					#The recursive part of the function (function called inside itself) 
					if self.backtracking(classer) == True:
						return True
					#Goes back a step (backtracks) and blanks the tile as the current board configuration must be invalid (the move does not result in the puzzle being solved)
					classer.sudoku_board[move_index[0]][move_index[1]][move_index[2]] = 0
					#blanks the screen & updates numbers
					self.screen.fill((255, 255, 255))
					self.add_rectangle()
			#returns False as there can't be a solution if the function arrives at this line
			return False	

def main():
	pan = Pane()
	pan.add_rectangle()
	pan.backtracking(bot)
	clock = pygame.time.Clock()
	while True:
		clock.tick(pan.FPS)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit(); sys.exit();

if __name__ == "__main__":
	main()

