import pygame
import sys
from pygame.locals import *
import random
import time


white = (255, 255, 255)
black = (0,0,0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

class Visualizer:
	def __init__(self, s = 50, t1 = "", t2 = ""):
		pygame.init()
		self.size = s
		self.DISPLAYSURF = pygame.display.set_mode((s*10, s*10))
		pygame.display.set_caption("Coding Clash!")

		self.col_to_col = {"r": red, "b": blue}
		self.piece_to_col = {"g":green, "t": black, "h":white}
		
		self.t1 = t1
		self.t2 = t2

	def playback(self, filename):
		with open(filename, "r") as file:
			boards = file.readlines()
		boards = [i[1:].strip() for i in boards if i[0]=="#"]
		boards = [[t[i:i+2] for i in range(0, len(t), 2)] for t in boards]
		#print(boards)
		boards = [[j[x*self.size:(x+1)*self.size] for x in range(self.size)] for j in boards]
		#print(boards)
		self.play(boards)
	
	def update(self, board):
		self.DISPLAYSURF.fill(white)
		for row in range(len(board)):
			for col in range(len(board)):
				if board[row][col]=="nn":
					continue
				else:
					pygame.draw.rect(self.DISPLAYSURF, self.col_to_col[board[row][col][0]], (10*row, 10*col, 10, 10))
					pygame.draw.rect(self.DISPLAYSURF, self.piece_to_col[board[row][col][1]], (10*row+2, 10*col+2, 6, 6))
	
	#def string_to_board(self, string):
	#	Eh no need

	def board_to_string(self, board):
		bout = [j for sub in board for j in sub]
		return "#"+"".join(bout)

	def save(self, board_states):
		#print(board_states)
		with open(str(id(self))+".txt", "w+") as file:
			file.write("\n".join(["|blue: "+self.t1, "|red: "+self.t2]+[self.board_to_string(b) for b in board_states]))


	def play(self, board_states):
		x = 0
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			if x<len(board_states):
				self.update(board_states[x])
			time.sleep(.2)
			x+=1
			pygame.display.update()
	
	def view(self, board):
		self.update(board)
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()

	def gen_random(self):
		board = [["nn" for i in range(self.size)] for j in range(self.size)]
		board[5][5] = "rh"
		board[45][45] = "bh"

		for i in range(100):
			x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
			if board[x][y]=="nn":
				board[x][y]=list(self.col_to_col.keys())[random.randint(0,1)]+list(self.piece_to_col.keys())[random.randint(0,1)]
		#print(board)
		return board


v = Visualizer()
#print(id(v))
#v.view(v.gen_random())
v.save([v.gen_random()])
v.playback("out.txt")

