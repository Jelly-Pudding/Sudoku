import copy
import numpy as np
import pygame, sys
from sudoku import Sudoku

bot = Sudoku()

def three_dimensions_to_one(num):
	if num == 0:
		#tranposes the 3d list so when it is converted to 1d, it fills in the board correctly
		original_numbers = np.transpose(bot.sudoku_board, axes=(1, 2, 0)).tolist()
	elif num == 1:
		original_numbers = bot.sudoku_board
	two_d_list = []
	for e1 in original_numbers:
		for e2 in e1:
			two_d_list.append(e2)
	one_d_list = []
	for e1 in two_d_list:
		for e2 in e1:
			one_d_list.append(e2)
	#Will store the indices of the original numbers in the puzzle (so as to differentiate them from the changing numbers in the backtracking function)
	original_index = []
	for index in range(len(one_d_list)):
		if one_d_list[index] != 0:
			original_index.append(index)
	return [original_index, one_d_list]

class Pane(object):
	def __init__(self):
		pygame.init()
		self.font = pygame.font.SysFont("Arial", 17)
		pygame.display.set_caption("Sudoku")	
		self.screen = pygame.display.set_mode((225, 225), 0, 32)
		self.screen.fill((255, 255, 255))
		pygame.display.update()
		self.FPS = 60
		self.original_index = []
		self.switch_number = 1
		#allows to skip initial for loops when backtracking to improve performance
		self.skip_for_loops = False
	def add_rectangle(self, mouse_x, mouse_y, num_input):
		if self.skip_for_loops == False:
			if self.switch_number == 10:
				self.switch_number = 1
			for i in range(1, 10, 1):
				for j in range(1, 10, 1):
					if mouse_x > i * 25 - 25 and mouse_x < i * 25 and mouse_y > j * 25 - 25 and mouse_y < j * 25:
						one_d_list = three_dimensions_to_one(1)[1]
						if j != 1:
							j = (j - 1) * 9 + 1
						#the delete key is pressed
						if num_input == 11:
							one_d_list[i + j - 2] = 0
						#the mouse is clicked
						elif num_input == 10:
							one_d_list[i + j - 2] = self.switch_number
						#a number is inputted
						else:
							one_d_list[i + j - 2] = num_input
						bot.sudoku_board = np.rollaxis(np.asarray(one_d_list).reshape(9, 3, 3), 0)
						self.switch_number += 1
						self.original_index = three_dimensions_to_one(0)[0]
		one_d_list = three_dimensions_to_one(0)[1]
		count = -1
		for i in range(0, 9, 1):
			for j in range(0, 9, 1):
				count +=1		
				self.rect = pygame.draw.rect(self.screen, ((0, 0, 0)), (i*25, j*25, 25, 25), 1)
				if count in self.original_index:
					self.screen.blit(self.font.render(str(one_d_list[count]), True, (0, 0, 0)), (i*25+7, j*25+2))
				elif one_d_list[count] != 0:
					self.screen.blit(self.font.render(str(one_d_list[count]), True, (0, 160, 160)), (i*25+7, j*25+2)) 				
				
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
					self.add_rectangle(mouse_x=1000, mouse_y=1000, num_input=-1)
					#The recursive part of the function (function called inside itself) 
					if self.backtracking(classer) == True:
						return True
					#Goes back a step (backtracks) and blanks the tile as the current board configuration must be invalid (the move does not result in the puzzle being solved)
					classer.sudoku_board[move_index[0]][move_index[1]][move_index[2]] = 0
			#returns False as there can't be a solution if the function arrives at this line
			return False	

def main():
	pan = Pane()
	pan.add_rectangle(0, 0, 0)
	#pan.backtracking(bot)
	clock = pygame.time.Clock()
	while True:
		clock.tick(pan.FPS)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit(); sys.exit();
			elif event.type == pygame.MOUSEBUTTONDOWN:
				num_input=10
				mouse_x, mouse_y = pygame.mouse.get_pos()
				pan.screen.fill((255, 255, 255))
				pan.add_rectangle(mouse_x, mouse_y, num_input)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
				num_input=1
				mouse_x, mouse_y = pygame.mouse.get_pos()
				pan.screen.fill((255, 255, 255))
				pan.add_rectangle(mouse_x, mouse_y, num_input)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
				num_input=2
				mouse_x, mouse_y = pygame.mouse.get_pos()
				pan.screen.fill((255, 255, 255))
				pan.add_rectangle(mouse_x, mouse_y, num_input)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
				num_input=3
				mouse_x, mouse_y = pygame.mouse.get_pos()
				pan.screen.fill((255, 255, 255))
				pan.add_rectangle(mouse_x, mouse_y, num_input)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
				num_input=4
				mouse_x, mouse_y = pygame.mouse.get_pos()
				pan.screen.fill((255, 255, 255))
				pan.add_rectangle(mouse_x, mouse_y, num_input)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_5:
				num_input=5
				mouse_x, mouse_y = pygame.mouse.get_pos()
				pan.screen.fill((255, 255, 255))
				pan.add_rectangle(mouse_x, mouse_y, num_input)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_6:
				num_input=6
				mouse_x, mouse_y = pygame.mouse.get_pos()
				pan.screen.fill((255, 255, 255))
				pan.add_rectangle(mouse_x, mouse_y, num_input)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_7:
				num_input=7
				mouse_x, mouse_y = pygame.mouse.get_pos()
				pan.screen.fill((255, 255, 255))
				pan.add_rectangle(mouse_x, mouse_y, num_input)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_8:
				num_input=8
				mouse_x, mouse_y = pygame.mouse.get_pos()
				pan.screen.fill((255, 255, 255))
				pan.add_rectangle(mouse_x, mouse_y, num_input)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_9:
				num_input=9
				mouse_x, mouse_y = pygame.mouse.get_pos()
				pan.screen.fill((255, 255, 255))
				pan.add_rectangle(mouse_x, mouse_y, num_input)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
				num_input=11
				mouse_x, mouse_y = pygame.mouse.get_pos()
				pan.screen.fill((255, 255, 255))
				pan.add_rectangle(mouse_x, mouse_y, num_input)			
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				bot.skip_for_loops = True
				pan.backtracking(bot)

if __name__ == "__main__":
	main()
