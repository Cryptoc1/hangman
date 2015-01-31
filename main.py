#!/usr/bin/env python
import random, os, sys

# Prompt Character
tch = "> "

# Some global variables
words = []
# Change the path below to wherever you cloned the wordlist
wordlist = open('/home/cryptoc1/Developer/python/Hangman/wordlist.txt', 'r')
underscore = []
guessed_letters = ["Guessed Letters: "]
bools = []

# Clears the screen
def clear():
    os.system("clear")

# Prompt that's shown upon program start-up
def init():
    clear()
    print tch + "Welcome to Hangman! To begin a new game, type 'start', or type 'exit' to exit this program."
    stdin = raw_input(tch)
    verify_input(stdin)

# The game 'loop'
def main():
    clear()
    print tch + "Hangman, the classic game."
    print tch + "Enter some letters."
    print get_underscores()
    print get_guessed_letters()
    stdin = get_stdin()
    if len(stdin) > 2:
        if stdin == "exit":
            verify_input("exit")
        elif stdin == "complete":
            print tch + "Congrats! You completed the game by finding the word: " + word + "!"
        else:
            print tch + "Please enter one letter at a time."
            main()
    else:
        check_letter(stdin, word)
        main()

# Shutsdown the program
def die():
    clear()
    sys.exit()

# Have the guessed all the letters in a the word?
def complete():
    string = str(get_underscores())
    string = string.replace("[", "")
    string = string.replace("]", "")
    string = string.replace("'", "")
    string = string.replace(" ", "")
    string = string.replace(",", "")
    if string == word:
        ret = True
    else:
        ret = False
    return ret

# Get a word from the wordlist
def choose_word():
    for line in wordlist.readlines():
        lines = line.replace("\n", "")
        lines = lines.replace("'", "")
        words.append(lines)
    wordlist.close()
    return words[random.randint(0, len(words) - 1)]

# Checks if an inputted letter is in the word
def check_letter(l, w):
    for i in range(0, len(bools)):
        if word[i] == l:
            bools[i] = True
    guessed_letters.append(l)

# Starts a new game
def new_game():
    clear()
    print tch + "New game started..."
    global word 
    word = choose_word()
    for char in word:
        underscore.append("_")
        bools.append(False)
    main()

# Formats and returns an array of underscores ('_') and correctly guessed letters
def get_underscores():
    indicies = []
    for i in range(0, len(bools)):
        if bools[i] == True:
            underscore[i] = word[i]
    return underscore

# Formats and returns an array of guessed letters
def get_guessed_letters():
    string = str(guessed_letters)
    string = string.replace("[", "")
    string = string.replace("]", "")
    string = string.replace("'", "")
    string = string.replace(",", " ")
    return string

# Gets input from the user if the word is completely guessed
def get_stdin():
    if complete():
        ret = "complete"
    else:
        ret = raw_input(tch).lower()
    return ret

# Checks if inputted text is an in-game command
def verify_input(stdin):
    new_stdin = str(stdin).lower()
    if new_stdin == "start":
        print tch + "Starting a new game..."
        new_game()
    elif new_stdin == "exit":
        print tch + "Exiting Hangman..."
        die()
    else:
        print tch + "Unrecgonized input."

# Start the game...
init()
