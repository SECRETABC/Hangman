#Hangman
#DOES IT WORK?
import time

import random

import os


def Title():

	print("Hangman")

	print('____')

	print('	|')

	time.sleep(1)



	print("Begin!!!")

	print("You got 7 tries")



	time.sleep(0.5)

	Game()

	print()





def Game():


	file = open("data/words.txt", "r")
	#print(f.readline())
	#print(f.readline())

	#for word in file:
  		#print(word)

	words = file.readlines()
	words = [word.strip() for word in words]
	words = random.choice(words)
	#words = random.choice(["Capitalism", "Adult", "Aeroplane", "Air", "Backpack", "Balloon", "Banana", "Radar", "Islam", "Quran", "Onomatopoeia"])



	Letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'



	#Lives

	hang = 7

	guess = ''



	while len(words) > 0:

		#message

		msg = ""

		loss = 0



		for l in words:

			if l in guess:

				msg = msg + l

			else:

				msg = msg + "_" + " "

				loss += 1

		if msg  == words:


			print(msg)

			print("CORRECT! The word is ", words)

			break

		print("Start Guessing! ", msg)

		g = input()



			#Invalid Input

		if g in Letters:

			guess = guess + g

		else:

			print("invalid input")

			g = input()



		if g not in words:

				hang = hang - 1

		if hang == 6:
			os.system('cls')

			print('____')

			print('	|')

			print("	o")

		if hang == 5:
			os.system('cls')

			print('____')

			print('    |')

			print("    o")

			print("    |")

		if hang == 4:
			os.system('cls')

			print('____')

			print('    |')

			print("    o")

			print("   -|")

		if hang == 3:
			os.system('cls')

			print('____')

			print('    |')

			print("    o")

			print("   -|-")

		if hang == 2:
			os.system('cls')

			print('____')

			print('    |')

			print("    o")

			print("   -|-")

			print("   /")

		if hang == 1:


			print('____')

			print('    |')

			print("    o")

			print("   -|-")

			print("   / \  ")

			print("You lose")
			print("The word is ", words)
			break

Title()
