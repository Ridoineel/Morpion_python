#! /usr/bin/env python3

from morpion import Morpion
from utils.style import *
import os

def main():

	game = Morpion()
	step = 0

	while game.winner == None:
		os.system("clear")

		player = step%2

		game.printChess()

		print(Style.bold(f"JOUEUR {player + 1}"))
		print("---------------")

		# ceil format (x, y)
		# put ceil in "x, y" or "x y" format
		inpt = input("Saisir une case ( 1-3, 1-3 ): ").strip()

		try:
			inpt = inpt.replace(",", " ")
			x, y = map(int, inpt.split())
		except:
			continue
		
		parsed_ceil = (x - 1)*3 + y - 1

		if game.play(player, parsed_ceil):
			# when user playing successfully
			step += 1
		else:
			print(Color.warning("Attention, case déjà joué"))

	game.printChess()

	print(f"Winner is player {game.winner + 1}")

if __name__ == '__main__':
	main()

