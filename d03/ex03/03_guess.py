# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    03_guess.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlewis-l <lerman.maggiel@gmail.com>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/27 13:13:56 by mlewis-l          #+#    #+#              #
#    Updated: 2018/06/27 13:13:58 by mlewis-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

WORD = ('apple', 'skips', 'laces', 'puppy', 'cases')
word = random.choice(WORD)
first_letter = word[0]
word_guess = ''
count = 1
limit = 10

print('Welcome to "Guess the Word Game!\n"')
print('You have 10 attempts at guessing letters in a word.\n')
print('There are 5 letters in the word.\n')
print('Let\'s begin!\n')
print('This word starts with the letter {}\n'.format(first_letter))
while count < limit and word_guess != word:
    word_guess = input('Guess #{}:\n'.format(count)).lower()

    if word_guess == word:
        print('Good Job! You are one with the Source.')
        break
    else:
            if len(word_guess) != len(word):
                print("0, 1, 2, 3, 4 that’s how we count to five!")
                count += 1
            else:
                if word_guess[0] != word[0]:
                    print('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                    print('Remember, the first letter of this word is {}.\n We won\'t count that guess ... try again!'.format(first_letter))
                else:
                    print('Nope! You have {} guesses left'.format(limit - count))
                    count += 1
print('\n')
print('The correct answer was {}.'.format(word))
print('\n')
input('Press Enter to leave the program')