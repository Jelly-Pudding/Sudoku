import pygame, sys
from sudoku import Sudoku
from sudoku import backtracking

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

#bot.printer()
#backtracking(bot)

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
		text = self.font.render("0", True, ((225, 0, 0)))
		for i in range(0, 9, 1):
			for j in range(0, 9, 1):
				self.rect = pygame.draw.rect(self.screen, ((0, 0, 0)), (i*25, j*25, 25, 25), 1)
				self.screen.blit(self.font.render("0", True, (255, 0, 0)), (i*25+7, j*25+2)) 				


		self.line = pygame.draw.line(self.screen, ((0, 0, 0)), (75, 0), (75, 225), 4)
		self.line = pygame.draw.line(self.screen, ((0, 0, 0)), (150, 0), (150, 225), 4)
		self.line = pygame.draw.line(self.screen, ((0, 0, 0)), (0, 75), (225, 75), 4)
		self.line = pygame.draw.line(self.screen, ((0, 0, 0)), (0, 150), (225, 150), 4)


		pygame.display.update()
	def add_text(self):
		#for i in range(0, 9, 1):
			#for j in range(0, 9, 1):
				#if i < 3:
					#self.screen.blit(self.font.render("3", True, (255, 0, 0)), (27*i +5 , j*25.7))
				#elif i < 6:
					#self.screen.blit(self.font.render("4", True, (255, 0, 0)), (27*i, j*25.6))
				#else:
					#self.screen.blit(self.font.render("5", True, (255, 0, 0)), (26*i, j*25.3))
		pygame.display.update()

def main():
	pan = Pane()
	pan.add_rectangle()
	pan.add_text()
	clock = pygame.time.Clock()
	while True:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit(); sys.exit();

if __name__ == "__main__":
	main()
