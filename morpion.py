from utils.Class import Color, Style

class Morpion:

	def __init__(self):
		self.chess = ["."]*9
		self.winner = None
		self.win_line = []

		print("Morpion Game architecture")

		for i in range(0, 9, 3):
			print(i, i + 1, i + 2, sep="  ")

		print()

	def play(self, player: int, ceil: int):
		# target: (int, int)
		
		if player not in [0, 1]:
			return

		# ceil = x*3 + y

		if self.chess[ceil] == ".":
			self.chess[ceil] = ["0", "X"][player]

			self.checkWinner()
		else:
			return -1

	def checkWinner(self):
		winner = False
		win_lines = [
			[0, 1, 2],
			[3, 4, 5],
			[6, 7, 8],
			[0, 3, 6],
			[1, 4, 7],
			[2, 5, 8],
			[0, 4, 8],
			[2, 4, 6],
		]

		for i in win_lines:
			containt = "".join([self.chess[i[k]] for k in range(3)])

			if len(set(containt)) == 1 and "." not in containt:
				# win
				self.win_line = i
				winner_symbol = containt[0]
				winner = [0, 1][winner_symbol == "X"]

				self.winner = winner

				return winner

		# no win
		return None

	def printChess(self, size=2):
		size = min(size, 10)

		# first line
		first_line = "\u250C" +  "\u2500"*(size*3) + "\u252C" + "\u2500"*(size*3) + "\u252C" + "\u2500"*(size*3) + "\u2510"
		# last line
		last_line = "\u2514" +  "\u2500"*(size*3) + "\u2534" + "\u2500"*(size*3) + "\u2534" + "\u2500"*(size*3) + "\u2518"
		# separator line
		separator_line = "\u251C" +  "\u2500"*(size*3) + "\u253C" + "\u2500"*(size*3) + "\u253C" + "\u2500"*(size*3) + "\u2524"


		print()
		print(first_line)

		for i in range(0, 9, 3):

			abc = self.chess[i:i+3]
			space_left = (size*3)//2
			space_right = size*3 - space_left - 1

			line = "\u2502" + (" "*space_left + "%s" + " "*space_right  + "\u2502")*3

			# for c in self.chess[i:i+3]:
			# 	if c == ".": 
			# 		c = " "

			for k in range(3):
				if abc[k] == ".":
					abc[k] = " "
				elif abc[k] == "X":
					abc[k] = Style.bold(Color.primary("X"))
				else:
					abc[k] = Style.bold(Color.success("O"))

				if (i + k) in self.win_line:
					abc[k] = Style.blink(abc[k])

			print(line % tuple(abc))

			if i != 6:
				print(separator_line)

		print(last_line)

		print()