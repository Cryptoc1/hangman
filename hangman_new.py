#!/usr/bin/env python

import random, os, sys

tch = "> "

words = []
wordlist = open('wordlist.txt', 'r')
underscore = []
bools = []

def clear():
    os.system("clear")

def init():
    clear()
    print tch + "Welcome to Hangman! To begin a new game, type 'start', to view more options, type 'help' or '?'."
    stdin = raw_input(tch)
    verify_input(stdin)

def main():
    print tch + "Enter some letters."
    print print_underscores()
    stdin = raw_input(tch).lower()
    if len(stdin) > 2:
        if stdin == "help" or stdin == "?":
            verify_input("?")
        elif stdin == "exit":
            verify_input("exit")
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

def choose_word():
    for line in wordlist.readlines():
        lines = line.replace("\n", "")
        lines = lines.replace("'", "")
        words.append(lines)
    wordlist.close()
    return words[random.randint(0, len(words) - 1)]

def check_letter(l, w):
    for letter in w:
        if letter == l:
            bools[w.index(l)] = True
            print bools

def new_game():
    clear()
    print tch + "New game started..."
    global word 
    word = choose_word()
    for char in word:
        underscore.append("_")
        bools.append(False)

    # TODO: This line is for debugging
    print word
    main()

def print_underscores():
    indices = []
    for i in bools:
        if i == True:
            indices.append(bools.index(i))
        print indices
    for i in indices:
        underscore[i] = word[i]
    return underscore

def verify_input(stdin):
    new_stdin = str(stdin).lower()
    if new_stdin == "start":
        print tch + "Starting a new game..."
        new_game()
    elif new_stdin == "exit":
        print tch + "Exiting Hangman..."
        die()
    elif new_stdin == "help" or new_stdin == "?":
        help()
    else:
        help()

init()
