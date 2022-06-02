from utils.style import *

class Morpion:
	def __init__(self):
		# chess is list[9]
		# ceil from 0 to 8

		self.chess = ["."]*9
		self.winner = None
		self.win_line = []

	def play(self, player: int, ceil: int):
		if self.chess[ceil] != ".":
			return False

		if player == 0:
			self.chess[ceil] = "O"
		elif player == 1:
			self.chess[ceil] = "X"

		self.checkWinner()

		return True

	def checkWinner(self):
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
			a, b, c = i

			line = self.chess[a] + self.chess[b] + self.chess[c]

			if "." not in line and len(set(line)) == 1:
				# winner

				self.win_line = i

				if "O" in line:
					self.winner = 0
				else:
					self.winner = 1

		return self.winner

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

			for k in range(3):
				if abc[k] == ".":
					abc[k] = " "
				elif abc[k] == "X":
					abc[k] = Style.bold(Color.primary("X"))
				else:
					abc[k] = Style.bold(Color.success("O"))

				if (i + k) in self.win_line:
					abc[k] = Style.blink(abc[k])

			# line for size
			for _ in range(size - 1):
				print(line % (" ", " ", " "))

			# symbols line
			print(line % tuple(abc))

			# line for size
			for _ in range(size - 1):
				print(line % (" ", " ", " "))

			if i != 6:
				print(separator_line)

		print(last_line)

		print()