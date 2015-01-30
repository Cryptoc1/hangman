#!/usr/bin/env python

##################################################################
##################################################################
###                                                            ###
###     Hangman By Samuel Steele                               ###
###     Hangman is a simple python script that is meant        ###
###     to be run from the terminal. The rules are as          ###
###     the same as regular hangman, just in a bit different   ###
###     format.         Happy coding.                          ###
###                             -Cryptoc1                      ###
###                                                            ###
##################################################################
##################################################################

####START MODULE IMPORTS####
import random
####END MODULE IMPORTS####

#declare some viarables to get started
words = []
wordlist= open('wordlist.txt', 'r')
underscore = []
####START FUNCTIONS####

#the only function I'm going to comment in is main(), try to figure the rest out yourself

def pick_a_word():
        word_position = random.randint(0, len(words) - 1)
        return words[word_position]
def start():
        print "Welcome to hangman. To start playing type 'start'"
        start = raw_input(': ')
        if start == "start":
                    main()
        else:
                    error_input()
def error_input():
        print "Sorry what was that? If you are having trouble starting try typing 'start'"
        start = raw_input(':')
        if start == "start":
                    main()
        else:
                    error_input()
def main():
        #delete every newline character and apostrophe
        for line in wordlist.readlines():
                    lines = line.replace("\n", "")
                    lines = lines.replace("'", "")
                    words.append(lines)

        #call pick_a_word() to get a random word from our array
        word = pick_a_word()

        #print how many characters there our in the users word
        print "There are %s characters in your word." % len(word)

        #print underscores for each character in the word
        for char in word:
                underscore.append("_")

        print underscore
        print word
        #function that takes users input and does stuff to it
        def start_guessing():
                #take the input
                print "Start by typing one letter at a time."
                letter = raw_input(": ")
                #we'll use this in a second, promise
                guessed_letters = []
                #if the user input is a string, do that stuff (Know errors:apostrophes and such characters are considered strings)
                if isinstance(letter, basestring) == True:
                        for char in word:
                                #if a letter in the word is the same as the input, add it to the array
                                if char == letter:
                                        index = word.index(char)
                                        if index != True:
                                                print underscore
                                                start_guessing()                                                
                                        else:
                                                underscore[index] = char
                #that wasn't a string inputed...
                else:
                        print "Sorry, that wasn't a letter that you entered."
                        #restart the function to keep the script from ending if the user doesnt enter a string
                        start_guessing()
                #keep an array of the letters being guessed
                guessed_letters.append(letter)
                #give the user the first letter in the word for free (because I'm so nice)
                underscore[0] = word[0]
                print underscore
                print "Letters already guessed, %s" % guessed_letters
        
        ##a loop to keep the script running until the user has guessed the word
        for underscores in underscore:
                if underscores == "_":
                        still_guessing = True
                else:
                        still_guessing = False

        while still_guessing:
                start_guessing()
        ##end loop

####END FUNCTIONS####

##the game 'starts' here
start()
