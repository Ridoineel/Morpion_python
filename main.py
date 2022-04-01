#! /usr/bin/env python3

from morpion import Morpion
import os

def main():

	game = Morpion()

	step = 0
	while game.winner == None:
		os.system("clear")

		game.printChess()

		# ceil format (x, y)
		ceil = input(f"Player {step % 2} (1-3, 1-3): ").strip()
		ceil = ceil.replace(" ", ",")

		x, y = map(int, ceil.split(","))


		parsed_ceil = (x - 1)*3 + y - 1

		if game.play(step % 2, parsed_ceil) != -1:
			step += 1


	game.printChess()

	print(f"Winner is player {game.winner}")

if __name__ == '__main__':
	main()
