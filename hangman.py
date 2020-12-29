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
    for s in secret_word:
    	if s not in letters_guessed:
    		s = '_'
    	print(s, end=" ")


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
		print("Available letters: ")
		get_available_letters(letters_guessed)
		print("\nLetters in secret word: ")
		get_guessed_word(secret_word, letters_guessed)
		print()

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
			print("Nicely done: ")
			get_guessed_word(secret_word, letters_guessed)
		else:
			if user_letter_lower in vowels:
				guesses_left -= 2
				print("This vowel isn't in secret word")
			else:
				guesses_left -= 1
				print("Man, i'm sory to you but this letter isn't in my word.")
			get_guessed_word(secret_word, letters_guessed)

		if is_word_guessed(secret_word, letters_guessed) == True:
			print("\n\nCongratulations you won ! Your score is: ", guesses_left*len(set(letters_guessed)))
			break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
