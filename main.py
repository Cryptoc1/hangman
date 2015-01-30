#!/usr/bin/env python

################################################################
################################################################
###                                                          ###
###     Hangman by Samuel Steele                             ###
###     Hangman is a simple python game that runs in the     ###
###     Terminal. The rules are the same as the classic      ###
###     game.       Happy Coding,                            ###
###                     -Cryptoc1                            ###
###                                                          ###
################################################################
################################################################

import random, os, sys

tch = "> "

words = []
wordlist = open('wordlist.txt', 'r')
underscore = []
guessed_letters = ["Guessed Letters: "]
bools = []

def clear():
    os.system("clear")

def init():
    clear()
    print tch + "Welcome to Hangman! To begin a new game, type 'start', or type 'exit' to exit this program."
    stdin = raw_input(tch)
    verify_input(stdin)

def main():
    clear()
    print tch + "Hangman, the classic game."
    print tch + "Enter some letters."
    print print_underscores()
    print print_guessed_letters()
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

def die():
    clear()
    sys.exit()

def help():
    print tch + "\n" + tch + "\tstart :: Start a new game\n" + tch + "\texit :: Exit Hangman program\n" + tch + "\thelp or '?' :: Display this help dialog\n" + tch
    main()

def complete():
    string = str(print_underscores())
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

def choose_word():
    for line in wordlist.readlines():
        lines = line.replace("\n", "")
        lines = lines.replace("'", "")
        words.append(lines)
    wordlist.close()
    return words[random.randint(0, len(words) - 1)]

def check_letter(l, w):
    for i in range(0, len(bools)):
        if word[i] == l:
            bools[i] = True
    guessed_letters.append(l)

def new_game():
    clear()
    print tch + "New game started..."
    global word 
    word = choose_word()
    for char in word:
        underscore.append("_")
        bools.append(False)
    main()

def print_underscores():
    indicies = []
    for i in range(0, len(bools)):
        if bools[i] == True:
            underscore[i] = word[i]
    return underscore

def print_guessed_letters():
    string = str(guessed_letters)
    string = string.replace("[", "")
    string = string.replace("]", "")
    string = string.replace("'", "")
    string = string.replace(",", " ")
    return string

def get_stdin():
    if complete():
        ret = "complete"
    else:
        ret = raw_input(tch).lower()
    return ret

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

init()
