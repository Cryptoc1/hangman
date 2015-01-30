#!/usr/bin/python

import random

words = []
wordlist = open('wordlist.txt')
lives_remaining = 14
guessed_letters = ' '

for line in wordlist:
                    lines = line.replace("\n", "")
                    lines = lines.replace("'", "")
                    words.append(lines)

def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print("You win! Well done!")
            break
        if lives_remaining == 0:
            print ("You are hung!")
            print ("The word was: %s" % word)
            break

def pick_a_word():
    word_postition = random.randint(0, len(words) - 1)
    return words[word_postition]

def get_guess(word):
    print_word_with_blanks(word)
    print ("Lives Remaining: " + str(lives_remaining))
    guess = input(" Guess a letter or whole word: ")
    return guess

def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            display_word = display_word + letter
        else:
            display_word = display_word + "_"
    print(display_word)
    
def process_guess(guess, word):
    if len(guess) > 1:
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)

def whole_word_guess(guess, word):
    global lives_remaining
    if guess == word:
        return True
    else:
        return False

def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        lives_remaining = lives_remaining - 1
    guessed_letters = guessed_letters + guess
    if all_letters_guessed(word):
        return True
    return False

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter) == -1:
            return False
    return True

play()



