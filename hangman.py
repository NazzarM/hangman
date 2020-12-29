# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import collections


WORDLIST_FILENAME = "words.txt"


def load_words():
	print("Loading word list from file...")
	inFile = open(WORDLIST_FILENAME, 'r')
	line = inFile.readline()
	wordlist = line.split()
	print("  ", len(wordlist), "words loaded.")
	return wordlist



def choose_word(wordlist):
	return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
	if set(secret_word) == set(letters_guessed):
		return True
	else:
		return False



def get_guessed_word(secret_word, letters_guessed):
	temp = []
	string = ""
	for s in secret_word:
		if s not in letters_guessed:
			s = '_'
		temp.append(s)
	string = string.join(temp)
	return string


def get_available_letters(letters_guessed):
    for i in string.ascii_lowercase:
    	if i not in letters_guessed:
    		print(i, end=", ")
    
    

def hangman(secret_word):
	print("Welcome to the game hangman!")
	print("About this game: Do you know the rules?")
	print("In this game you have to answer the word that computer made up!")
	print("You have only 6 attempts and 3 warnings, so don't waste them all!.")
	print("If you lose all your attempts, computer will show his word.")
	print("I am thinking of a word that is ", len(secret_word), " letters long.")

	guesses_left = 6
	warnings_left = 3
	letters_guessed = []
	secret_word_list = []	
	vowels = ["a", "e", "i", "o", "u"]

	for character in secret_word:
		secret_word_list.append(character)

	while True:
		print()
		print('-'*40)
		print()
		if guesses_left == 0:
			print("Sorry! You wasted all your attempts, better luck next time:)")
			print("The secret word was ",secret_word)
			break
		print("Guesses left - ",guesses_left, ". Warnings left - ", warnings_left)	
		print("Available letters: ",)
		get_available_letters(letters_guessed)
		print("\nLetters in secret word: ", get_guessed_word(secret_word, letters_guessed))

		user_letter = input("\nEnter a letter: ")
		user_letter_lower = user_letter.lower()

		if user_letter_lower.isalpha() == False:
			if warnings_left == 0:
				guesses_left -= 1
				print("Sorry, but you wasted all your warnings. So now you have only ",guesses_left," guesses.")
				continue
			else:
				warnings_left -= 1
				print("Whoops! You lost your warning. Be careful next time.")
				continue

		if user_letter_lower in letters_guessed:
			if warnings_left == 0:
				guesses_left -= 1
				print("You have entered this letter already. So now you have only ",guesses_left," guesses.")
				continue
			else:
				warnings_left -= 1
				print("Minus one warning on your count. Try again.")
				continue

		else:
			letters_guessed.append(user_letter_lower)

		if user_letter_lower in secret_word_list:
			print("Nicely done: ",get_guessed_word(secret_word, letters_guessed))

		else:
			if user_letter_lower in vowels:
				guesses_left -= 2
				print("This vowel isn't in secret word")
			else:
				guesses_left -= 1
				print("Man, i'm sory to you but this letter isn't in my word. ",get_guessed_word(secret_word, letters_guessed))

		if is_word_guessed(secret_word, letters_guessed) == True:
			print("\n\nCongratulations you won ! Your score is: ", guesses_left*len(set(letters_guessed)))
			break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
	count = 0
	if not len(my_word) == len(other_word):
		return False
	else:
		for i in zip(my_word,other_word):
			if not i[0] == "_":
				if i[0] == i[1]:
					count += 1

	total = len(my_word) - count - my_word.count("_")
	
	if total == 0:
		return True
	else:
		return False

def show_possible_matches(my_word):
	for word in wordlist:
		if match_with_gaps(my_word, word):
			print(word, end =", ")



def hangman_with_hints(secret_word):
	print("Welcome to the game Hangman!")
	print("About this game: Do you know the rules?")
	print("In this game you have to answer the word that computer made up!")
	print("You have only 6 attempts and 3 warnings, so don't waste them all!.")
	print("If you lose all your attempts, computer will show his word. By the way, if you're stuck, use '*' to show all possible words!")
	print("I am thinking of a word that is ", len(secret_word), " letters long.")


	guesses = 6
	warnings = 3
	letters = []
	computer_word_list = []	
	we_are_vowels = ["a", "e", "i", "o", "u"]
	cheats = 0

	for symbol in secret_word:
		computer_word_list.append(symbol)

	while True:
		print()
		print('-'*40)
		print()
		if guesses == 0:
			print("Sorry! You wasted all your attempts, better luck next time:)")
			print("The secret word was ",secret_word)
			break
		print("Guesses left - ",guesses, ". Warnings left - ", warnings)	
		print("Available letters: ")
		get_available_letters(letters)
		print("\nLetters in secret word: ", get_guessed_word(secret_word, letters))

		ask_for_letter = input("\nEnter a letter: ")

		if cheats == 0:
			if ask_for_letter == "*":
				print("You've used the hint. Now you are god of this game (your set of guesses is now 1000000) ")
				guesses = 1000000
				print("Here's list of words that are similar to secret word: ")
				show_possible_matches(get_guessed_word(secret_word, letters))
				cheats += 1
		else:
			print("Sorry, but u've already used my help.")

		ask_for_letter_lower = ask_for_letter.lower()

		if guesses < 10:
			if ask_for_letter_lower.isalpha() == False:
				if warnings == 0:
					guesses -= 1
					print("Sorry, but you wasted all your warnings. So now you have only ",guesses," guesses.")
					continue
				else:
					warnings -= 1
					print("Whoops! You lost your warning. Be careful next time.")
					continue

		if ask_for_letter_lower in letters:
			if warnings == 0:
				guesses -= 1
				print("You have entered this letter already. So now you have only ",guesses," guesses.")
				continue
			else:
				warnings -= 1
				print("Minus one warning on your count. Try again.")
				continue
		else:
			letters.append(ask_for_letter_lower)

		if ask_for_letter_lower in computer_word_list:
			print("Nicely done: ", get_guessed_word(secret_word, letters))
		else:
			if ask_for_letter_lower in we_are_vowels:
				guesses -= 2
				print("This vowel isn't in secret word")
			else:
				guesses -= 1
				print("Man, i'm sory to you but this letter isn't in my word.", get_guessed_word(secret_word, letters))

		if len(letters) == len(secret_word):
			print("\n\nCongratulations you won ! Your score is: ", len(set(letters)))
			break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = "apple"
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
